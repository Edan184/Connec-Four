import asyncio, websockets

@app.route('/connect_four', methods=['GET'])
def connect_four():
    if session_info() is not False:  
        # Checks for session cookie, if not present, redirects to login   
        payload = session_info()[0][0]
        return render_template('connect_four.html', title='Connect Four!', ip=ip_query(), user=payload[1], name=payload[2])
    else:
        return redirect(url_for('login'))
