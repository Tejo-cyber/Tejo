const generateFoodBlog = async () => {
    const prompt = "Write a food blog about Italian cuisine.";
    const response = await fetch("http://127.0.0.1:5000/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ prompt })
    });
    const data = await response.json();
    if (data.blog) {
        console.log(data.blog); // Display the generated blog
    } else {
        console.error(data.error);
    }
};

generateFoodBlog();
