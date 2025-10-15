#!/usr/bin/env python3
"""
Website Optimization Script for Production
Minifies CSS, obfuscates JavaScript, and adds code protection
"""

import re
import os
import shutil
from pathlib import Path

def minify_css(css_content):
    """Minify CSS by removing comments, whitespace, and unnecessary characters"""
    # Remove comments
    css_content = re.sub(r'/\*.*?\*/', '', css_content, flags=re.DOTALL)
    
    # Remove unnecessary whitespace
    css_content = re.sub(r'\s+', ' ', css_content)
    
    # Remove spaces around specific characters
    css_content = re.sub(r'\s*([{}:;,>+~])\s*', r'\1', css_content)
    
    # Remove trailing semicolons before }
    css_content = re.sub(r';\s*}', '}', css_content)
    
    # Remove unnecessary quotes
    css_content = re.sub(r'([^\\])\'([^\']*?[^\\])\'', r'\1\2', css_content)
    css_content = re.sub(r'([^\\])"([^"]*?[^\\])"', r'\1\2', css_content)
    
    return css_content.strip()

def obfuscate_js_variables(js_content):
    """Basic JavaScript obfuscation by renaming variables and functions"""
    
    # Dictionary to store original->obfuscated mappings
    var_map = {}
    counter = 0
    
    def get_obfuscated_name():
        nonlocal counter
        # Generate short, meaningless names
        chars = 'abcdefghijklmnopqrstuvwxyz'
        name = ''
        temp = counter
        while True:
            name = chars[temp % 26] + name
            temp //= 26
            if temp == 0:
                break
        counter += 1
        return '_' + name
    
    # Find and replace function names
    function_pattern = r'\bfunction\s+([a-zA-Z_$][a-zA-Z0-9_$]*)\s*\('
    
    def replace_function(match):
        func_name = match.group(1)
        if func_name not in var_map:
            var_map[func_name] = get_obfuscated_name()
        return f'function {var_map[func_name]}('
    
    js_content = re.sub(function_pattern, replace_function, js_content)
    
    # Find and replace variable declarations
    var_pattern = r'\b(?:let|const|var)\s+([a-zA-Z_$][a-zA-Z0-9_$]*)'
    
    def replace_var(match):
        var_name = match.group(1)
        if var_name not in ['currentSlideIndex', 'autoSlideInterval', 'totalSlides', 'slideInterval']:  # Keep some essential names
            if var_name not in var_map:
                var_map[var_name] = get_obfuscated_name()
            return match.group(0).replace(var_name, var_map[var_name])
        return match.group(0)
    
    js_content = re.sub(var_pattern, replace_var, js_content)
    
    # Replace function calls and variable usage
    for original, obfuscated in var_map.items():
        # Replace standalone occurrences
        js_content = re.sub(rf'\b{re.escape(original)}\b', obfuscated, js_content)
    
    return js_content

def minify_js(js_content):
    """Minify JavaScript by removing comments and unnecessary whitespace"""
    # Remove single-line comments (but preserve URLs)
    js_content = re.sub(r'(?<!:)//.*$', '', js_content, flags=re.MULTILINE)
    
    # Remove multi-line comments
    js_content = re.sub(r'/\*.*?\*/', '', js_content, flags=re.DOTALL)
    
    # Remove unnecessary whitespace
    js_content = re.sub(r'\s+', ' ', js_content)
    
    # Remove spaces around operators and punctuation
    js_content = re.sub(r'\s*([{}();,:])\s*', r'\1', js_content)
    
    return js_content.strip()

def add_code_protection(html_content):
    """Add JavaScript code to prevent inspection and copying"""
    
    protection_script = '''
<script>
// Disable right-click context menu
document.addEventListener('contextmenu', function(e) {
    e.preventDefault();
    return false;
});

// Disable F12, Ctrl+Shift+I, Ctrl+U, Ctrl+S
document.addEventListener('keydown', function(e) {
    // F12
    if (e.keyCode === 123) {
        e.preventDefault();
        return false;
    }
    // Ctrl+Shift+I (Developer Tools)
    if (e.ctrlKey && e.shiftKey && e.keyCode === 73) {
        e.preventDefault();
        return false;
    }
    // Ctrl+U (View Source)
    if (e.ctrlKey && e.keyCode === 85) {
        e.preventDefault();
        return false;
    }
    // Ctrl+S (Save)
    if (e.ctrlKey && e.keyCode === 83) {
        e.preventDefault();
        return false;
    }
    // Ctrl+Shift+C (Inspect Element)
    if (e.ctrlKey && e.shiftKey && e.keyCode === 67) {
        e.preventDefault();
        return false;
    }
});

// Disable text selection
document.addEventListener('selectstart', function(e) {
    e.preventDefault();
    return false;
});

// Disable drag and drop
document.addEventListener('dragstart', function(e) {
    e.preventDefault();
    return false;
});

// Clear console periodically
setInterval(function() {
    console.clear();
}, 1000);

// Detect DevTools
let devtools = {open: false, orientation: null};
setInterval(function() {
    if (window.outerHeight - window.innerHeight > 200 || window.outerWidth - window.innerWidth > 200) {
        if (!devtools.open) {
            devtools.open = true;
            console.clear();
            document.body.innerHTML = '<h1 style="text-align:center;margin-top:200px;">Developer tools detected. Please close them to continue.</h1>';
        }
    } else {
        if (devtools.open) {
            devtools.open = false;
            location.reload();
        }
    }
}, 500);
</script>'''
    
    # Insert protection script before closing head tag
    html_content = html_content.replace('</head>', protection_script + '\n</head>')
    
    return html_content

def create_production_build():
    """Create optimized production version of the website"""
    
    print("🚀 Starting production optimization...")
    
    # Create dist directory
    dist_dir = Path('dist')
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    dist_dir.mkdir()
    
    # Copy images and documents
    for folder in ['images', 'documents']:
        if Path(folder).exists():
            shutil.copytree(folder, dist_dir / folder)
    
    # Read and process CSS
    print("📦 Minifying CSS...")
    with open('style.css', 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    minified_css = minify_css(css_content)
    
    with open(dist_dir / 'style.min.css', 'w', encoding='utf-8') as f:
        f.write(minified_css)
    
    # Read and process HTML
    print("🔧 Processing HTML...")
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Extract JavaScript from HTML
    js_pattern = r'<script>(.*?)</script>'
    js_matches = re.findall(js_pattern, html_content, re.DOTALL)
    
    if js_matches:
        print("🔒 Obfuscating JavaScript...")
        js_content = js_matches[0]
        
        # Obfuscate and minify JavaScript
        obfuscated_js = obfuscate_js_variables(js_content)
        minified_js = minify_js(obfuscated_js)
        
        # Replace in HTML
        html_content = re.sub(js_pattern, f'<script>{minified_js}</script>', html_content, flags=re.DOTALL)
    
    # Update CSS reference
    html_content = html_content.replace('style.css?v=5', 'style.min.css')
    
    # Add code protection
    print("🛡️  Adding code protection...")
    html_content = add_code_protection(html_content)
    
    # Minify HTML
    print("📄 Minifying HTML...")
    # Remove comments
    html_content = re.sub(r'<!--.*?-->', '', html_content, flags=re.DOTALL)
    
    # Remove unnecessary whitespace (but preserve some formatting)
    html_content = re.sub(r'\n\s*\n', '\n', html_content)
    html_content = re.sub(r'>\s+<', '><', html_content)
    
    # Write optimized HTML
    with open(dist_dir / 'index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # Copy other files that might be needed
    for file in ['README.md', 'requirements.txt']:
        if Path(file).exists():
            shutil.copy(file, dist_dir)
    
    print("✅ Production build complete!")
    print(f"📁 Optimized files are in the '{dist_dir}' directory")
    print("\n📊 Optimization Summary:")
    
    # Calculate size reductions
    original_css_size = os.path.getsize('style.css')
    optimized_css_size = os.path.getsize(dist_dir / 'style.min.css')
    css_reduction = ((original_css_size - optimized_css_size) / original_css_size) * 100
    
    original_html_size = os.path.getsize('index.html')
    optimized_html_size = os.path.getsize(dist_dir / 'index.html')
    html_reduction = ((original_html_size - optimized_html_size) / original_html_size) * 100
    
    print(f"CSS: {original_css_size:,} bytes → {optimized_css_size:,} bytes ({css_reduction:.1f}% reduction)")
    print(f"HTML: {original_html_size:,} bytes → {optimized_html_size:,} bytes ({html_reduction:.1f}% reduction)")
    
    print("\n🔒 Security features added:")
    print("• Right-click disabled")
    print("• Developer tools detection")
    print("• Keyboard shortcuts blocked")
    print("• Text selection disabled")
    print("• Console clearing")
    print("• Code obfuscation")

if __name__ == "__main__":
    create_production_build()