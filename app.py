import os
from flask import Flask, request, jsonify
from mfperfquery import mf_data

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY")  # optional, set in Render if you want to secure the endpoint

@app.route("/")
def home():
    return "Moneycontrol Mutual Fund API is running"

@app.route("/compare", methods=["GET"])
def compare_funds():
    # Optional simple API key check
    if API_KEY:
        key = request.args.get("key")
        if not key or key != API_KEY:
            return jsonify({"error": "Unauthorized (missing/invalid key)"}), 401

    fund_a_url = request.args.get("fundA")
    fund_b_url = request.args.get("fundB")

    if not fund_a_url or not fund_b_url:
        return jsonify({"error": "Both fundA and fundB query parameters are required"}), 400

    try:
        a = mf_data(fund_a_url)
        b = mf_data(fund_b_url)

        def normalize(d):
            return {
                "fund_name": d.get("Fund Name"),
                "category": d.get("Category"),
                "expense_ratio": d.get("Expense Ratio (%)"),
                "cagr_3y": d.get("3 Year Return (%)"),
                "cagr_5y": d.get("5 Year Return (%)"),
                "cagr_10y": d.get("10 Year Return (%)", "N/A"),
                "std_dev_3y": d.get("Standard Deviation (3Y)"),
                "beta": d.get("Beta"),
                "sharpe_ratio_3y": d.get("Sharpe Ratio (3Y)")
            }

        return jsonify({"fundA": normalize(a), "fundB": normalize(b)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
