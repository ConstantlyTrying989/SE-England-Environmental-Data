# SE England Environmental Data

Track weather and air quality for South East England. Collect data, spot trends, understand your environment.

---

## Quick Start
```bash
git clone https://github.com/ConstantlyTrying989/se-england-environmental-data.git
cd se-england-environmental-data
python -m venv venv
venv\Scripts\activate          # Windows or: source venv/bin/activate
pip install -r requirements.txt
python main.py
```

Done! Data collected, processed, and analyzed. 🎉

---

## What We Track

- 🌡️ Temperature, humidity, wind, pressure
- 💨 Air quality (PM2.5, PM10, NO₂, ozone)
- 📈 Trends and averages
- 📉 Min/max daily readings

---

## Purpose and Nature of Project
```bash
python main.py                    # Do everything
python scripts/data_collector.py  # Just collect data
python scripts/data_processor.py  # Just analyze data
python scripts/visualizer.py      # Just show charts
```

---

## Future Improvements

- Real weather API connections
- Interactive web dashboard
- Email alerts for bad air quality
- Maps showing pollution hotspots
- AI-powered weather predictions
- Mobile app

---

## Issues

**"Missing requests module?"**
```bash
pip install requests
```

**"Virtual environment not activating?"**
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

**Found a bug?** Open an issue on GitHub

**Want to contribute?** Fork, make changes, submit PR

---

## License

MIT - Use it however you want

---

Made to understand South East England's environment...