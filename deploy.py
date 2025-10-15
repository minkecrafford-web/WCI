#!/usr/bin/env python3
"""
Deployment helper script for production website
"""

import os
import zipfile
from pathlib import Path
import datetime

def create_deployment_package():
    """Create a deployment-ready ZIP package"""
    
    print("📦 Creating deployment package...")
    
    # Create timestamp for package name
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    package_name = f"western-cape-industrial-website_{timestamp}.zip"
    
    # Create ZIP package
    with zipfile.ZipFile(package_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add all files from dist directory
        dist_path = Path('dist')
        for root, dirs, files in os.walk(dist_path):
            for file in files:
                file_path = Path(root) / file
                # Store relative path without 'dist/' prefix
                arcname = file_path.relative_to(dist_path)
                zipf.write(file_path, arcname)
    
    print(f"✅ Deployment package created: {package_name}")
    print(f"📁 Package size: {os.path.getsize(package_name):,} bytes")
    
    return package_name

def print_deployment_instructions():
    """Print instructions for deploying the website"""
    
    instructions = """
🚀 DEPLOYMENT INSTRUCTIONS
========================

Your website is now optimized and ready for production!

📁 Production Files Location: ./dist/

🔒 Security Features Implemented:
• Code minification and obfuscation
• Right-click disabled
• Developer tools detection and blocking
• Keyboard shortcuts blocked (F12, Ctrl+U, etc.)
• Text selection disabled
• Console clearing
• DevTools detection with page redirect

📊 File Optimization:
• CSS reduced by 28.0%
• HTML reduced by 33.6%
• JavaScript obfuscated and minified

🌐 HOSTING OPTIONS:

1. STATIC HOSTING (Recommended):
   • Netlify: Drag and drop the 'dist' folder
   • Vercel: Connect to GitHub and deploy
   • GitHub Pages: Upload files to gh-pages branch
   • AWS S3 + CloudFront: Upload to S3 bucket

2. TRADITIONAL WEB HOSTING:
   • Upload all files from 'dist' folder to your web root
   • Ensure index.html is in the root directory
   • Make sure images/ and documents/ folders are uploaded

3. QUICK DEPLOYMENT COMMANDS:

   For Netlify CLI:
   npm install -g netlify-cli
   netlify deploy --prod --dir=dist

   For Vercel CLI:
   npm install -g vercel
   cd dist && vercel --prod

⚠️  IMPORTANT NOTES:
• Use HTTPS hosting for better security
• The protection measures work best on modern browsers
• Some corporate networks may override these protections
• Consider adding server-side protections for additional security

🔧 MAINTENANCE:
• Run 'python3 optimize.py' after any changes
• Test the production build before deploying
• Keep source files separate from production files

💡 ADDITIONAL SECURITY (Optional):
• Add Content Security Policy headers
• Enable HSTS on your server
• Use a CDN for additional DDoS protection
• Consider adding rate limiting
"""
    
    print(instructions)

def main():
    """Main deployment preparation function"""
    
    # Check if dist directory exists
    if not Path('dist').exists():
        print("❌ Error: dist directory not found. Run 'python3 optimize.py' first.")
        return
    
    # Create deployment package
    package_name = create_deployment_package()
    
    # Print instructions
    print_deployment_instructions()
    
    print(f"\n✅ Your website is ready for deployment!")
    print(f"📦 Deployment package: {package_name}")
    print(f"📁 Production files: ./dist/")

if __name__ == "__main__":
    main()