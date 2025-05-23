# Interactive Web-Based OS Simulator

Hey there! 👋 Welcome to our Interactive Web-Based OS Simulator. This project brings operating system concepts to life through an engaging web interface. Whether you're a student learning OS concepts or a developer interested in process scheduling and deadlock detection, this simulator is designed to make learning fun and interactive!

## 🌟 What's Inside?

### Process Scheduling Simulator
We've implemented four popular scheduling algorithms that you can experiment with:

1. **First-Come-First-Serve (FCFS)**
   - The classic scheduling algorithm
   - Processes are executed in the order they arrive
   - Perfect for understanding basic scheduling concepts

2. **Shortest Job First (SJF)**
   - Optimizes for minimum waiting time
   - Executes the shortest job first
   - Great for learning about optimization in scheduling

3. **Priority Scheduling**
   - Assigns priorities to processes
   - Higher priority processes get executed first
   - Ideal for understanding priority-based systems

4. **Round Robin Scheduling**
   - Uses time quantum for fair process execution
   - Perfect for learning about time-sharing systems
   - Great visualization of CPU time distribution

### Resource Allocation Graph (RAG) Simulator
Our RAG simulator is a powerful tool for understanding resource management and deadlock scenarios:

#### Core Features
- 🎯 Create processes and resources visually
- 🔄 Add request and allocation edges
- ⚠️ Detect deadlocks in real-time
- 🎨 Visual feedback for deadlocked nodes
- 📊 Clear distinction between processes and resources

#### Advanced Features
- ⏱️ **Starvation Detection**
  - Monitor process waiting times
  - Set custom thresholds for starvation detection
  - Get alerts for processes waiting too long
  - Track resource allocation patterns

- 🔍 **Deadlock Analysis**
  - Real-time cycle detection
  - Visual highlighting of deadlocked processes
  - Detailed cycle information
  - Easy-to-understand deadlock visualization

- 📈 **Resource Management**
  - Track resource allocation
  - Monitor process requests
  - Visualize resource dependencies
  - Reset and clear graph for new scenarios

## 🛠️ Tech Stack

### Frontend
- **HTML5 & CSS3**: For structure and styling
- **JavaScript (ES6+)**: For interactive features
- **Vis.js**: Powers our beautiful graph visualizations
- **Tailwind CSS**: Makes our UI responsive and modern

### Backend
- **Python 3.x**: Our main programming language
- **Flask**: Powers our web framework
- **NetworkX**: Handles graph operations and deadlock detection
- **Matplotlib**: Creates those awesome Gantt charts

## 📁 Project Structure

```
Interactive-Web-Based-OS-Simulator/
├── app.py                  # Main Flask application
├── graph.py               # Graph generation utilities
├── vercel.json            # Vercel deployment config
├── static/
│   ├── css/
│   │   └── style.css      # Custom styles
│   └── js/
│       ├── index.js       # Main JavaScript logic
│       ├── algorithm.js   # Algorithm-specific logic
│       └── rag.js         # RAG simulator logic
├── templates/
│   ├── index.html         # Home page
│   ├── program.html       # Algorithm simulation page
│   └── rag.html           # RAG simulator page
└── README.md              # This documentation
```

## 🚀 Getting Started

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Interactive-Web-Based-OS-Simulator.git
   cd Interactive-Web-Based-OS-Simulator
   ```

2. **Set up your environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Unix or MacOS:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Visit `http://localhost:5000`

### Using the Simulator

#### Process Scheduling
1. Select your preferred algorithm from the home page
2. Enter the number of processes
3. Fill in the details:
   - Arrival time
   - Burst time
   - Priority (for Priority Scheduling)
   - Time quantum (for Round Robin)
4. Click "Start" to see the magic happen!
5. Explore the Gantt chart and performance metrics

#### RAG Simulator
1. Add processes and resources using the input fields
2. Create connections between processes and resources
3. Click "Check for Deadlock" to analyze the graph
4. Watch as the simulator highlights any deadlocked nodes

## 🌐 Deployment

This project is deployed on Vercel. The deployment configuration is handled by `vercel.json`, which includes:
- Python 3.11 runtime
- Proper routing for Flask
- Environment variables
- Memory and duration limits

## 🤝 Contributing

We love contributions! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Vis.js](https://visjs.org/) for the amazing graph visualizations
- [NetworkX](https://networkx.org/) for graph operations
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Tailwind CSS](https://tailwindcss.com/) for the beautiful UI
- [Vercel](https://vercel.com/) for hosting

## 📞 Contact

Have questions or suggestions? Feel free to:
- Open an issue
- Submit a pull request
- Reach out to us through GitHub

## 🔗 Links

- [Live Demo](https://interactive-os-simulator.vercel.app)
- [GitHub Repository](https://github.com/yourusername/Interactive-Web-Based-OS-Simulator)

---

Made with ❤️ for the OS learning community