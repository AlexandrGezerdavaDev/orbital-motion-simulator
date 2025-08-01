# Orbital Motion Simulator 🚀

A Python-based simulator for modeling orbital mechanics, visualizing satellite orbits around Earth, and calculating orbital maneuvers. This project provides a simple yet extensible framework for simulating 2D and 3D orbits with cool plots and animations! 🌍

## Features ✨
- **Orbit Simulation**: Computes orbital trajectories using numerical integration of the two-body problem. 🪐
- **Visualization**: Generates 3D static plots and animations of orbits using Matplotlib. 📊
- **Orbital Maneuvers**: Calculates velocity changes (Δv) for Hohmann transfers between circular orbits. 🚀
- **Extensibility**: Modular design makes it easy to add new features, like elliptical orbits or complex maneuvers. 🔧
- **Robust Visualization**: Handles both 2D (planar) and 3D orbits smoothly. 🎨

## Project Structure 📁
```
orbital-motion-simulator/
├── src/
│   ├── main.py              # Main script to run the simulation
│   ├── physics.py           # Orbital dynamics calculations
│   ├── visualization.py     # 3D plotting and animation
│   ├── maneuvers.py         # Orbital maneuver calculations (e.g., Hohmann transfer)
├── examples/
│   ├── sample_orbit.py     # Example script to demonstrate usage
├── requirements.txt         # Python dependencies
├── README.md               # Project documentation
├── LICENSE                 # MIT License
├── .gitignore              # Git ignore file
```

## Requirements 🛠️
- Python 3.8+
- Libraries listed in `requirements.txt`:
  - `numpy==1.26.4`
  - `scipy==1.14.1`
  - `matplotlib==3.9.2`

## Installation ⚙️
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/orbital-motion-simulator.git
   cd orbital-motion-simulator
   ```
2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the sample simulation**:
   ```bash
   python examples/sample_orbit.py
   ```

## Usage 🎮
The simulator models a satellite orbiting Earth and visualizes its trajectory in 3D. It also calculates Δv for a Hohmann transfer to a higher orbit. To customize the simulation:

1. **Modify initial conditions** in `src/main.py`:
   - Adjust `r0` (position), `v0` (velocity), `mu` (gravitational parameter), or `t_span` (time span).
   - Example: Add a z-component to `r0` or `v0` for a 3D orbit! 🌌
2. **Run the simulation**:
   ```bash
   python src/main.py
   ```
3. **Output**:
   - A static 3D plot of the orbit. 📈
   - An animated 3D visualization of the satellite’s motion. 🎥
   - Console output of Δv values (e.g., `Δv1 = 638.79 m/s, Δv2 = 584.09 m/s`). 🖨️

## Example 🌟
The `examples/sample_orbit.py` script simulates a satellite in a circular orbit at 7000 km radius and calculates a Hohmann transfer to a 10,000 km orbit. To run:
```bash
python examples/sample_orbit.py
```
Watch the orbit come to life with a 3D animation! 🎬

## Contributing 🤝
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

Please keep the code style consistent and add tests if possible. Let’s make this simulator even better together! 😊

## License 📜
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Future Improvements 🔮
- Add support for elliptical orbits. 🥚
- Implement more maneuvers (e.g., bi-elliptic transfers, plane changes). 🚀
- Add unit tests with `pytest` for reliability. ✅
- Enhance visuals with customizable styles or interactive controls. 🎨

## Contact 📬
For questions or ideas, open an issue on GitHub or reach out to oleksandrgezerdava@gmail.com Happy orbiting! 🌠

---
*Last updated: August 2025*