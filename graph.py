import matplotlib
matplotlib.use('Agg')  # Set the non-interactive backend 'Agg'
import os
import matplotlib.pyplot as plt
import io
import base64

font = {
    'font.family': 'sans-serif',
    'font.sans-serif': ['system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Open Sans', 'Helvetica Neue', 'sans-serif'],
    'font.weight': 'bold'
}

def graph(name, start_time, end_time, n):
    plt.figure(figsize=(10, 5))
    for i in range(n):
        plt.barh(i, end_time[i] - start_time[i], left=start_time[i], color='gray', height=0.3)
        # Configure font
        matplotlib.rcParams.update(font)
        # Background color of the chart
        plt.gca().set_facecolor((0.18, 0.18, 0.18)) 
        # Color of lines
        plt.gca().spines['bottom'].set_color('white')
        plt.gca().spines['left'].set_color('white')
        plt.gca().spines['top'].set_color((0.18, 0.18, 0.18))
        plt.gca().spines['right'].set_color((0.18, 0.18, 0.18))
        # Color of axes
        plt.xlabel('X Axis', color='white')
        plt.ylabel('Y Axis', color='white')
        # Change color of axis labels
        plt.xticks(color='white')
        plt.yticks(color='white')

    # Configure labels and title
    plt.xlabel('Time')
    plt.ylabel('Process')
    plt.title(name, color='white', fontweight='bold', fontsize=20)
    plt.yticks(range(n), [f'Process {i + 1}' for i in range(n)])
    plt.legend()

    # Save to memory buffer instead of file
    buf = io.BytesIO()
    plt.savefig(buf, format='png', facecolor=(0.18, 0.18, 0.18))
    plt.close()
    buf.seek(0)
    
    # Convert to base64
    return base64.b64encode(buf.getvalue()).decode('utf-8')
    
def graphRound(name, execution_sequence, n):
    plt.figure(figsize=(10, 5))
    for i, (process, start, end) in enumerate(execution_sequence):
        plt.barh(process, end - start, left=start, color='gray', height=0.3)
        # Configure font
        matplotlib.rcParams.update(font)
        # Background color of the chart
        plt.gca().set_facecolor((0.18, 0.18, 0.18)) 
        # Color of lines
        plt.gca().spines['bottom'].set_color('white')
        plt.gca().spines['left'].set_color('white')
        plt.gca().spines['top'].set_color((0.18, 0.18, 0.18))
        plt.gca().spines['right'].set_color((0.18, 0.18, 0.18))
        # Color of axes
        plt.xlabel('X Axis', color='white')
        plt.ylabel('Y Axis', color='white')
        # Change color of axis labels
        plt.xticks(color='white')
        plt.yticks(color='white')

    # Configure labels and title
    plt.xlabel('Time')
    plt.ylabel('Process')
    plt.title(name, color='white', fontweight='bold', fontsize=20)
    plt.yticks(range(n), [f'Process {process + 1}' for process in range(n)])
    plt.legend()

    # Save to memory buffer instead of file
    buf = io.BytesIO()
    plt.savefig(buf, format='png', facecolor=(0.18, 0.18, 0.18))
    plt.close()
    buf.seek(0)
    
    # Convert to base64
    return base64.b64encode(buf.getvalue()).decode('utf-8')
