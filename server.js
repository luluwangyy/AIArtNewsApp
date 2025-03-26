app.post('/api/validate-referral', (req, res) => {
    const { referralCode } = req.body;
    
     
    const validReferralCodes = {
        'lulu': true,
        '12345': true
         
    };

    if (validReferralCodes[referralCode]) {
        // Return API keys from environment variables
        res.json({
            success: true,
            replicateApiKey: process.env.REPLICATE_API_TOKEN,
            openaiApiKey: process.env.OPENAI_API_KEY
        });
    } else {
        res.json({
            success: false,
            message: 'Invalid referral code'
        });
    }
});

 