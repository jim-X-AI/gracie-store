import os

# Define the file contents
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Luxeloom Fashion Wear</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header -->
    <header>
        <div class="container">
            <img src="logo.png" alt="Luxeloom Logo" class="logo">
            <nav>
                <ul>
                    <li><a href="#home">Home</a></li>
                    <li><a href="#about">About Us</a></li>
                    <li><a href="#projects">Project</a></li>
                    <li><a href="#contact">Contact Us</a></li>
                </ul>
                <button class="signup-btn">Sign Up</button>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section id="hero">
        <div class="container">
            <h1>Fashion and Wears Collection</h1>
            <p>Omnis directa al deshabilitate de un nov lingua franca...</p>
            <div class="buttons">
                <button class="shop-now">Shop Now</button>
                <button class="discover-collection">Discover Collection</button>
            </div>
            <div class="image-gallery">
                <!-- Image thumbnails -->
            </div>
        </div>
    </section>

    <!-- Product Showcase -->
    <section id="products">
        <div class="container">
            <!-- New Best Seller -->
            <!-- About Us -->
        </div>
    </section>

    <!-- Client Testimonials -->
    <section id="testimonials">
        <div class="container">
            <!-- Carousel of testimonials -->
        </div>
    </section>

    <!-- Discount Section -->
    <section id="discount">
        <div class="container">
            <!-- Discount offer -->
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container">
            <!-- Footer content -->
        </div>
    </footer>
</body>
</html>
"""

css_content = """
/* styles.css */
body {
    font-family: 'Arial', sans-serif;
    margin: 0;
    padding: 0;
    background-color: #FFD700;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

header {
    background-color: #FFF;
    padding: 20px 0;
}

.logo {
    width: 50px;
    height: 50px;
    border-radius: 10px;
    margin-right: 20px;
}

.nav ul {
    list-style: none;
    display: flex;
    gap: 20px;
}

.nav li a {
    text-decoration: none;
    color: #333;
}

.signup-btn {
    background-color: #FFA500;
    color: #FFF;
    border: none;
    padding: 10px 20px;
    border-radius: 20px;
    cursor: pointer;
}

#hero {
    text-align: center;
    padding: 50px 0;
}

#hero h1 {
    font-size: 48px;
    color: #333;
}

#hero p {
    font-size: 16px;
    color: #666;
    margin: 20px 0;
}

.buttons button {
    padding: 10px 20px;
    border-radius: 20px;
    margin: 10px;
    cursor: pointer;
}

.shop-now {
    background-color: #000;
    color: #FFF;
}

.discover-collection {
    background-color: #FFF;
    color: #000;
    border: 1px solid #000;
}

@media (max-width: 768px) {
    .container {
        padding: 10px;
    }

    header nav ul {
        flex-direction: column;
    }

    #hero {
        padding: 30px 0;
    }
}
"""

js_content = """
// script.js
// Add interactivity here, such as a testimonial carousel or hover effects.
console.log("JavaScript loaded successfully!");
"""

# Create the files
def create_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)

# Create the project directory if it doesn't exist
project_dir = "luxeloom"
os.makedirs(project_dir, exist_ok=True)

# Change to the project directory
os.chdir(project_dir)

# Generate the files
create_file("index.html", html_content)
create_file("styles.css", css_content)
create_file("script.js", js_content)

print("Files created successfully!")