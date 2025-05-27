
from flask import Flask, request, jsonify
from neo4j import GraphDatabase
import os

app = Flask(__name__)

# --- Neo4j Configuration ---
NEO4J_URI = os.environ.get("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.environ.get("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD", "neo4j123")

try:
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    # Verify connection
    with driver.session() as session:
        session.run("RETURN 1")
    print("Successfully connected to Neo4j")
except Exception as e:
    print(f"Failed to connect to Neo4j: {str(e)}")
    raise

# --- Routes ---

# Create a Process Node
@app.route('/process/<name>', methods=['POST'])
def create_process(name):
    try:
        with driver.session() as session:
            session.run("MERGE (p:Process {name: $name})", name=name)
        return jsonify({"status": "Process created", "name": name})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Create a Resource Node
@app.route('/resource/<name>', methods=['POST'])
def create_resource(name):
    try:
        with driver.session() as session:
            session.run("MERGE (r:Resource {name: $name})", name=name)
        return jsonify({"status": "Resource created", "name": name})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Create REQUEST edge from Process → Resource
@app.route('/request', methods=['POST'])
def request_resource():
    data = request.get_json()
    with driver.session() as session:
        session.run("""
            MATCH (p:Process {name: $process}), (r:Resource {name: $resource})
            MERGE (p)-[:REQUESTS]->(r)
        """, process=data['process'], resource=data['resource'])
    return jsonify({"status": "Request edge created"})

# Create ALLOCATED_TO edge from Resource → Process
@app.route('/allocate', methods=['POST'])
def allocate_resource():
    data = request.get_json()
    with driver.session() as session:
        session.run("""
            MATCH (r:Resource {name: $resource}), (p:Process {name: $process})
            MERGE (r)-[:ALLOCATED_TO]->(p)
        """, resource=data['resource'], process=data['process'])
    return jsonify({"status": "Allocation edge created"})


# Get the current graph (nodes and edges)
@app.route('/graph', methods=['GET'])
def get_graph():
    with driver.session() as session:
        result = session.run("""
            MATCH (n)-[r]->(m)
            RETURN labels(n)[0] AS from_type, n.name AS from_node, 
                   type(r) AS relation, 
                   labels(m)[0] AS to_type, m.name AS to_node
        """)
        edges = []
        for record in result:
            edges.append({
                "from": record["from_node"],
                "from_type": record["from_type"],
                "to": record["to_node"],
                "to_type": record["to_type"],
                "relation": record["relation"]
            })
    return jsonify(edges)


# Deadlock Detection
@app.route('/deadlocks', methods=['GET'])
def detect_deadlocks():
    with driver.session() as session:
        # Improved deadlock detection query
        result = session.run("""
            MATCH cycle = (p1:Process)-[:REQUESTS]->(:Resource)-[:ALLOCATED_TO]->(p2:Process)
            WHERE p1 <> p2
            WITH p1, p2, cycle
            MATCH (r2:Resource)-[:ALLOCATED_TO]->(p1)
            WHERE (p2)-[:REQUESTS]->(r2)
            RETURN [node in nodes(cycle) | node.name] as cycle_nodes
            LIMIT 1
        """)
        record = result.single()
        if record:
            cycle = record["cycle_nodes"]
            return jsonify({
                "deadlock": True,
                "cycle": cycle,
                "message": "🚨 Deadlock detected in this cycle."
            })
        return jsonify({
            "deadlock": False,
            "message": "✅ No deadlock detected."
        })

if __name__ == '__main__':
    app.run(debug=True)
