# Business Website Template

A simple, professional one-page business website template using HTML, CSS, and Python.

## Project Structure

```
business-website/
├── index.html          # Main webpage
├── style.css           # Styling
├── main.py            # Python web server
├── requirements.txt   # Python dependencies
├── images/           # Folder for your images
└── README.md         # This file
```

## How to Use

### 1. Add Your Images
Place your business images in the `images/` folder:
- `logo.png` - Your business logo (50x50px recommended)
- `hero_logo.jpg` - Hero section logo/image (600x550px recommended)
- `water-splash.png` - Water splash background for hero (PNG with transparency recommended)
- `hero-image.jpg` - Main banner image (optional)
- `service1.jpg` through `service7.jpg` - Service images for each service
- Product images: `ebra.jpg`, `vacuum-pumps.jpg`, `progressive-cavity-pump.jpg`, `gear-pump.jpg`, `aodd-pump.jpg`, `lobe-pumps.jpg`, `electrical-motors.jpg`, `gearboxes.jpg`, `dosing-pumps.jpg`, `industrial-fans.jpg`, `chlorine-dioxide.jpg`, `float-switches.jpg`, `vsd-drives.jpg`
- Any other images you want to use

### 2. Customize the Content
Edit `index.html` to:
- Replace "Your Business Name" with your actual business name
- Update the services section with your actual services
- Change contact information
- Modify the about section

### 3. Adjust the Styling
Edit `style.css` to:
- Change colors to match your brand
- Modify fonts and spacing
- Adjust the layout as needed

### 4. Run the Website

#### Option 1: Using Python Server
```bash
python3 main.py
```
This will start a local server at `http://localhost:8000` and automatically open your browser.

#### Option 2: Simple Python Server
```bash
python3 -m http.server 8000
```

#### Option 3: Just Open in Browser
You can also directly open `index.html` in your web browser.

## Features

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Professional Styling**: Clean, modern business appearance
- **Simple Navigation**: Smooth scrolling to sections
- **Contact Section**: Easy-to-find contact information
- **Service Showcase**: Highlight your key services
- **Image-Heavy Product Showcase**: Visually striking grid layout featuring large product images with hover effects
- **Logo Integration**: Business logo displayed next to company name
- **Fast Loading**: Minimal dependencies, fast performance

## Customization Tips

1. **Colors**: The main colors are defined in the CSS. Look for color codes like `#2c3e50`, `#3498db`, etc.
2. **Images**: Ensure your images are web-optimized (JPG/PNG, reasonable file sizes)
3. **Content**: Keep text concise and focused on your value proposition
4. **Call-to-Action**: Update the "Get Started" button to link to your desired action

## Need Help?

- HTML basics: Edit text content and structure in `index.html`
- CSS basics: Modify colors, fonts, and layout in `style.css`
- Python basics: The server file `main.py` handles serving your website locally