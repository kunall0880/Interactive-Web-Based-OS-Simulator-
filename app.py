from flask import Flask, render_template, request

from graph import graph , graphRound

app = Flask(__name__)

# Vercel requires this handler
@app.route("/api/<path:path>", methods=['GET', 'POST'])
def api_handler(path):
    return app.handle_request(request)

@app.route("/", methods=['POST', 'GET'])
def home():
    return render_template("index.html")

@app.route("/fifo", methods=['POST', 'GET'])
def fifo():
    if request.method == 'GET':
        n = 0
    if request.method == 'POST':
        n = int(request.form['n'])
        if n != 0:
            data = request.form
            last_data = list(data.items())[-1]
            if last_data[0] == 'start':
                arrival_time = []
                burst_time = []
                CPU = 0
                for i in range(n):
                    arrival_time.append(int(request.form.get('at' + str(i))))
                    burst_time.append(int(request.form.get('bt' + str(i))))
                ATt = [0] * n
                NoP = n  # number of Processes
                waiting_time = [0] * n
                turnaround_time = [0] * n
                start_time = [0] * n
                end_time = [0] * n

                for i in range(n):
                    ATt[i] = arrival_time[i]

                while NoP > 0 :
                    for i in range(n):
                        if ATt[i] <= CPU:
                            waiting_time[i] = CPU - arrival_time[i]
                            start_time[i] = CPU 
                            CPU += burst_time[i]
                            end_time[i] = CPU
                            turnaround_time[i] = CPU - arrival_time[i]
                            ATt[i] = float('inf')
                            NoP -= 1
                            break
                    else:
                        CPU += 1
                
                graph_base64 = graph('FIFO GRAPH',start_time,end_time,n)
                    
                return render_template("program.html", n=n, bt=burst_time, at=arrival_time, wt=waiting_time,
                                       tat=turnaround_time, AvgWT=round((sum(waiting_time) / n), 2),
                                       AVGTaT=round((sum(turnaround_time) / n), 2), table=True, name='FIFO',
                                       graph=graph_base64)

    return render_template("program.html", n=n, table=False, name='FIFO')

@app.route("/sjf", methods=['POST', 'GET'])
def sjf():
    if request.method == 'GET':
        n = 0
    if request.method == 'POST':
        n = int(request.form['n'])
        if n != 0:
            data = request.form
            last_data = list(data.items())[-1]
            if last_data[0] == 'start':
                arrival_time = []
                burst_time = []
                for i in range(n):
                    arrival_time.append(int(request.form.get('at' + str(i))))
                    burst_time.append(int(request.form.get('bt' + str(i))))
                CPU = 0
                start_time = [0] * n
                end_time = [0] * n
                ATt = [0] * n
                NoP = n  # number of Processes
                waiting_time = [0] * n
                turnaround_time = [0] * n
                processed = [False] * n

                for i in range(n):
                    ATt[i] = arrival_time[i]

                while NoP > 0:
                    min_burst = float('inf')
                    min_index = -1
                    for i in range(n):
                        if ATt[i] <= CPU and not processed[i] and burst_time[i] < min_burst:
                            min_burst = burst_time[i]
                            min_index = i

                    if min_index == -1:
                        CPU += 1
                    else:
                        waiting_time[min_index] = CPU - arrival_time[min_index]
                        start_time[min_index] = CPU
                        CPU += burst_time[min_index]
                        end_time[min_index] = CPU
                        turnaround_time[min_index] = CPU - arrival_time[min_index]
                        processed[min_index] = True
                        NoP -= 1

                graph_base64 = graph('SJF GRAPH',start_time,end_time,n)

                return render_template("program.html", n=n, bt=burst_time, at=arrival_time, wt=waiting_time,
                                       tat=turnaround_time, AvgWT=round((sum(waiting_time) / n), 2),
                                       AVGTaT=round((sum(turnaround_time) / n), 2),
                                       table=True, name='SJF', graph=graph_base64)

    return render_template("program.html", n=n, table=False, name='SJF')

@app.route("/priority", methods=['POST', 'GET'])
def priority():
    if request.method == 'GET':
        n = 0
    if request.method == 'POST':
        n = int(request.form['n'])
        if n != 0:
            data = request.form
            last_data = list(data.items())[-1]
            if last_data[0] == 'start':
                arrival_time = []
                burst_time = []
                priority = []
                CPU = 0
                for i in range(n):
                    arrival_time.append(int(request.form.get('at' + str(i))))
                    burst_time.append(int(request.form.get('bt' + str(i))))
                    priority.append(int(request.form.get('priority' + str(i))))
                ATt = [0] * n
                NoP = n  # number of Processes
                PPt = [0] * n
                waiting_time = [0] * n
                turnaround_time = [0] * n
                start_time = [0] * n
                end_time = [0] * n

                for i in range(n):
                    PPt[i] = priority[i]
                    ATt[i] = arrival_time[i]

                LAT = max(arrival_time)
                for i in range(n):
                    if arrival_time[i] > LAT:
                        LAT = arrival_time[i]

                while NoP > 0 and CPU <= 1000:
                    min_priority = float('inf')  # Initialize with positive infinity
                    min_priority_index = -1
                    min_arrival_time = float('inf')
                    for i in range(n):
                        if ATt[i] <= CPU and PPt[i] != (LAT + 10) and PPt[i] < min_priority:
                            min_priority = PPt[i]
                            min_priority_index = i
                            min_arrival_time = arrival_time[i]
                        elif ATt[i] <= CPU and PPt[i] != (LAT + 10) and PPt[i] == min_priority and arrival_time[i] < min_arrival_time:
                            min_priority_index = i
                            min_arrival_time = arrival_time[i]
                            
                    if min_priority_index == -1:
                        CPU += 1
                    else:
                        start_time[min_priority_index] = CPU
                        waiting_time[min_priority_index] = CPU - arrival_time[min_priority_index]
                        CPU += burst_time[min_priority_index]
                        end_time[min_priority_index] = CPU
                        turnaround_time[min_priority_index] = CPU - arrival_time[min_priority_index]
                        ATt[min_priority_index] = LAT + 10
                        PPt[min_priority_index] = LAT + 10
                        NoP -= 1

                graph_base64 = graph('PRIORITY GRAPH',start_time,end_time,n)

                return render_template("program.html", prio=priority, n=n, bt=burst_time, at=arrival_time, wt=waiting_time,
                                       tat=turnaround_time, AvgWT=round((sum(waiting_time) / n), 2), AVGTaT=round((sum(turnaround_time) / n), 2),
                                       table=True, name='PRIORITY', graph=graph_base64)

    return render_template("program.html", n=n, table=False, name='PRIORITY')

@app.route("/roundRobin", methods=['POST', 'GET'])
def roundRobin():
    if request.method == 'GET':
        n = 0
        time_quantum = 0
    if request.method == 'POST':
        n = int(request.form['n'])
        time_quantum = int(request.form['tq'])
        if n != 0:
            data = request.form
            last_data = list(data.items())[-1]
            if last_data[0] == 'start':
                arrival_time = []
                burst_time = []
                for i in range(n):
                    arrival_time.append(int(request.form.get('at' + str(i))))
                    burst_time.append(int(request.form.get('bt' + str(i))))
                CPU = 0
                waiting_time = [0] * n
                turnaround_time = [0] * n
                remaining_burst_time = burst_time.copy()
                arrival_time_aux = arrival_time.copy()
                nAux = n
                processed = [False] * n
                NoP = n
                execution_sequence = []  # List to store the execution sequence of processes

                while any(remaining_burst_time):
                    
                    if NoP == 0:
                        processed = [False] * n
                        NoP = nAux
                    min_arrival = float('inf')
                    index = -1
                    for i in range(n):
                        if remaining_burst_time[i] > 0 and arrival_time_aux[i] <= CPU and not processed[i] and arrival_time_aux[i] < min_arrival:
                            min_arrival = arrival_time_aux[i]
                            index = i 
                            
                    if index == -1:
                        CPU += 1
                    else:
                        execute_time = min(time_quantum, remaining_burst_time[index])           
                        waiting_time[index] += CPU - arrival_time[index]
                        CPU += execute_time
                        remaining_burst_time[index] -= execute_time
                        turnaround_time[index] += CPU - arrival_time[index]
                        arrival_time[index] = CPU
                        NoP -= 1
                        processed[index] = True
                        if remaining_burst_time[index] == 0:
                            nAux -= 1 
                        
                        # Save the process execution in the execution sequence list
                        if len(execution_sequence) > 0 and execution_sequence[-1][0] == index:
                            # If the last process in the list is the same as the current one,
                            # update the finish time of the previous process
                            execution_sequence[-1] = (index, execution_sequence[-1][1], CPU)
                        else:
                            # If it's a new process, add it to the list
                            execution_sequence.append((index, CPU - execute_time, CPU))
                

                graph_base64 = graphRound('ROUND ROBIN GRAPH',execution_sequence,n)

                return render_template("program.html", time_quantum=time_quantum, n=n, bt=burst_time, at=arrival_time_aux, wt=waiting_time,
                                       tat=turnaround_time, AvgWT= round((sum(waiting_time) / n), 2), AVGTaT=round((sum(turnaround_time) / n), 2),
                                       table=True, name='ROUND ROBIN', graph=graph_base64)
    return render_template("program.html", time_quantum=time_quantum, n=n, table=False, name='ROUND ROBIN')


if __name__ == "__main__":
    app.run(debug=True)
else:
    # This is required for Vercel
    handler = app