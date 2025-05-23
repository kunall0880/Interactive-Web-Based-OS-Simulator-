// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log('Initializing RAG simulator...');
    
    // Initialize the network
    const container = document.getElementById('rag-graph');
    if (!container) {
        console.error('Graph container not found!');
        return;
    }
    
    console.log('Creating network...');
    const data = {
        nodes: new vis.DataSet(),
        edges: new vis.DataSet()
    };
    
    const options = {
        nodes: {
            shape: 'dot',
            size: 30,
            font: {
                size: 16
            }
        },
        edges: {
            arrows: 'to',
            smooth: {
                type: 'cubicBezier'
            }
        },
        physics: {
            stabilization: false,
            barnesHut: {
                gravitationalConstant: -80000,
                springConstant: 0.001,
                springLength: 200
            }
        }
    };
    
    try {
        const network = new vis.Network(container, data, options);
        console.log('Network created successfully');
        
        // Add event listeners
        console.log('Adding event listeners...');
        
        // Add process button
        const addProcessBtn = document.getElementById('add-process');
        if (addProcessBtn) {
            addProcessBtn.addEventListener('click', addProcess);
            console.log('Add process button listener added');
        } else {
            console.error('Add process button not found!');
        }
        
        // Add resource button
        const addResourceBtn = document.getElementById('add-resource');
        if (addResourceBtn) {
            addResourceBtn.addEventListener('click', addResource);
            console.log('Add resource button listener added');
        } else {
            console.error('Add resource button not found!');
        }
        
        // Add request edge button
        const addRequestBtn = document.getElementById('add-request');
        if (addRequestBtn) {
            addRequestBtn.addEventListener('click', addRequestEdge);
            console.log('Add request button listener added');
        } else {
            console.error('Add request button not found!');
        }
        
        // Add allocation edge button
        const addAllocationBtn = document.getElementById('add-allocation');
        if (addAllocationBtn) {
            addAllocationBtn.addEventListener('click', addAllocationEdge);
            console.log('Add allocation button listener added');
        } else {
            console.error('Add allocation button not found!');
        }
        
        // Check deadlock button
        const checkDeadlockBtn = document.getElementById('check-deadlock');
        if (checkDeadlockBtn) {
            checkDeadlockBtn.addEventListener('click', checkDeadlock);
            console.log('Check deadlock button listener added');
        } else {
            console.error('Check deadlock button not found!');
        }
        
        // Check starvation button
        const checkStarvationBtn = document.getElementById('check-starvation');
        if (checkStarvationBtn) {
            checkStarvationBtn.addEventListener('click', checkStarvation);
            console.log('Check starvation button listener added');
        } else {
            console.error('Check starvation button not found!');
        }
        
        console.log('All event listeners added successfully');
        
    } catch (error) {
        console.error('Error initializing network:', error);
        alert('Error initializing the graph. Please check the console for details.');
    }
});

// Function to add a process to the RAG
async function addProcess() {
    const processId = document.getElementById('process-id').value;
    console.log('Adding process:', processId); // Debug log
    
    if (!processId) {
        console.error('Process ID is empty');
        alert('Please enter a process ID');
        return;
    }
    
    try {
        console.log('Sending request to /rag/add_node'); // Debug log
        const response = await fetch('/rag/add_node', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                id: processId,
                type: 'process'
            })
        });
        
        console.log('Response status:', response.status); // Debug log
        
        if (response.ok) {
            const result = await response.json();
            console.log('Server response:', result); // Debug log
            
            data.nodes.add({ 
                id: processId, 
                label: processId, 
                color: { background: 'white' },
                shape: 'dot'
            });
            document.getElementById('process-id').value = '';
            
            // Update process select dropdown
            const processSelect = document.getElementById('process-select');
            const option = document.createElement('option');
            option.value = processId;
            option.textContent = processId;
            processSelect.appendChild(option);
            
            console.log('Process added successfully'); // Debug log
        } else {
            const error = await response.json();
            console.error('Server error:', error); // Debug log
            alert('Failed to add process: ' + (error.message || 'Unknown error'));
        }
    } catch (error) {
        console.error('Error adding process:', error);
        alert('Error adding process: ' + error.message);
    }
}

// Function to add a resource to the RAG
async function addResource() {
    const resourceId = document.getElementById('resource-id').value;
    console.log('Adding resource:', resourceId); // Debug log
    
    if (!resourceId) {
        console.error('Resource ID is empty');
        alert('Please enter a resource ID');
        return;
    }
    
    try {
        console.log('Sending request to /rag/add_node'); // Debug log
        const response = await fetch('/rag/add_node', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                id: resourceId,
                type: 'resource'
            })
        });
        
        console.log('Response status:', response.status); // Debug log
        
        if (response.ok) {
            const result = await response.json();
            console.log('Server response:', result); // Debug log
            
            data.nodes.add({ 
                id: resourceId, 
                label: resourceId, 
                color: { background: 'white' },
                shape: 'diamond'
            });
            document.getElementById('resource-id').value = '';
            
            // Update resource select dropdown
            const resourceSelect = document.getElementById('resource-select');
            const option = document.createElement('option');
            option.value = resourceId;
            option.textContent = resourceId;
            resourceSelect.appendChild(option);
            
            console.log('Resource added successfully'); // Debug log
        } else {
            const error = await response.json();
            console.error('Server error:', error); // Debug log
            alert('Failed to add resource: ' + (error.message || 'Unknown error'));
        }
    } catch (error) {
        console.error('Error adding resource:', error);
        alert('Error adding resource: ' + error.message);
    }
}

// Function to add a request edge
async function addRequestEdge() {
    const processId = document.getElementById('process-select').value;
    const resourceId = document.getElementById('resource-select').value;
    
    if (processId && resourceId) {
        try {
            const response = await fetch('/rag/add_edge', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    source: processId,
                    target: resourceId,
                    type: 'request'
                })
            });
            
            if (response.ok) {
                data.edges.add({
                    from: processId,
                    to: resourceId,
                    arrows: 'to',
                    color: { color: 'blue' }
                });
            }
        } catch (error) {
            console.error('Error adding request edge:', error);
        }
    }
}

// Function to add an allocation edge
async function addAllocationEdge() {
    const resourceId = document.getElementById('resource-select').value;
    const processId = document.getElementById('process-select').value;
    
    if (processId && resourceId) {
        try {
            const response = await fetch('/rag/add_edge', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    source: resourceId,
                    target: processId,
                    type: 'allocation'
                })
            });
            
            if (response.ok) {
                data.edges.add({
                    from: resourceId,
                    to: processId,
                    arrows: 'to',
                    color: { color: 'green' }
                });
            }
        } catch (error) {
            console.error('Error adding allocation edge:', error);
        }
    }
}

// Function to show popup
function showPopup(title, message) {
    const overlay = document.getElementById('popup-overlay');
    const popupTitle = document.getElementById('popup-title');
    const popupMessage = document.getElementById('popup-message');
    const closeButton = document.getElementById('popup-close');

    popupTitle.textContent = title;
    popupMessage.textContent = message;
    overlay.classList.remove('hidden');

    closeButton.onclick = function() {
        overlay.classList.add('hidden');
    };

    // Close popup when clicking outside
    overlay.onclick = function(e) {
        if (e.target === overlay) {
            overlay.classList.add('hidden');
        }
    };
}

// Function to check for deadlocks
async function checkDeadlock() {
    try {
        const nodes = data.nodes.get();
        const edges = data.edges.get();
        
        const response = await fetch('/rag/check_deadlock', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                nodes: nodes.map(node => node.id),
                edges: edges.map(edge => ({
                    from: edge.from,
                    to: edge.to
                }))
            })
        });
        
        if (response.ok) {
            const result = await response.json();
            if (result.deadlock) {
                // Highlight nodes involved in the deadlock
                for (const nodeId of result.nodes) {
                    data.nodes.update({ id: nodeId, color: { background: 'red' } });
                }
                document.getElementById('deadlock-result').innerText = 'Deadlock detected!';
                showPopup('Deadlock Detected', `Deadlock detected among: ${result.nodes.join(', ')}`);
            } else {
                // Reset node colors
                for (const node of nodes) {
                    data.nodes.update({ id: node.id, color: { background: 'white' } });
                }
                document.getElementById('deadlock-result').innerText = 'No deadlock detected.';
                showPopup('No Deadlock', 'No deadlock detected in the current graph.');
            }
        }
    } catch (error) {
        console.error('Error checking for deadlock:', error);
        showPopup('Error', 'An error occurred while checking for deadlock.');
    }
}

// Function to check for starvation
async function checkStarvation() {
    try {
        const response = await fetch('/rag/check_starvation', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                threshold: 0
            })
        });
        
        if (response.ok) {
            const result = await response.json();
            const resultDiv = document.getElementById('starvation-result');
            
            if (result.starvation_detected) {
                // Highlight starving processes in blue
                for (const process of result.starving_processes) {
                    data.nodes.update({ 
                        id: process.process, 
                        color: { background: '#3b82f6' }  // Blue color
                    });
                }
                
                // Create detailed message
                const starvingList = result.starving_processes
                    .map(p => `${p.process} (waiting for ${p.wait_time} time units)`)
                    .join('\n');
                
                resultDiv.innerHTML = `
                    <div class="mt-4 p-4 bg-blue-50 border border-blue-200 rounded">
                        <p class="font-semibold text-blue-800">Starvation Detected!</p>
                        <p class="text-blue-700 mt-2">The following processes are starving:</p>
                        <ul class="list-disc list-inside mt-2 text-blue-700">
                            ${result.starving_processes.map(p => 
                                `<li>${p.process} (waiting for ${p.wait_time} time units)</li>`
                            ).join('')}
                        </ul>
                    </div>
                `;
                
                showPopup('Starvation Detected', 
                    `The following processes are starving:\n${starvingList}`);
            } else {
                // Reset node colors
                const nodes = data.nodes.get();
                for (const node of nodes) {
                    if (node.shape === 'dot') {  // Only reset process nodes
                        data.nodes.update({ id: node.id, color: { background: 'white' } });
                    }
                }
                
                resultDiv.innerHTML = `
                    <div class="mt-4 p-4 bg-green-50 border border-green-200 rounded">
                        <p class="text-green-800">No starvation detected.</p>
                    </div>
                `;
                
                showPopup('No Starvation', 'No processes are currently starving.');
            }
        }
    } catch (error) {
        console.error('Error checking for starvation:', error);
        showPopup('Error', 'An error occurred while checking for starvation.');
    }
} 