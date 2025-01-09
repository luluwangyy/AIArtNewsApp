const axios = require('axios');

const fetchOpenAICompletion = async (input) => {
    try {
        const data = {
            model: "gpt-3.5-turbo",
            messages: [
                { "role": "user", "content": input }
            ]
        };

        const config = {
            method: 'post',
            maxBodyLength: Infinity,
            url: 'https://api.openai.com/v1/chat/completions',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`
            },
            data: data,
            proxy: {
                host: "127.0.0.1",
                port: 13588,  // Ensure this matches your actual HTTP proxy port
                protocol: "http"
            }
        };

        const response = await axios(config);
        console.log("response.data:", JSON.stringify(response.data));
        return response.data.choices[0].message;
    } catch (error) {
        console.error("Error fetching OpenAI completion:", error);
        throw error;  // Rethrow or handle as needed
    }
};
