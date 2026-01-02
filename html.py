footer = """<p>&copy; 2025-2026 OpenHRX - <a href="/legal">Legal / License / Trademark</a> / <a href="/code">Code / OpenHRX for you</a> / <a href="https://www.openhrx.be">OpenHRX Website</a></p>
    <img src="/static/logo/oserver.png" alt="Powered by OpenHRX Server">"""

header = """
    <img src="/static/logo/oopenhrx-white.png" alt="(8)OpenHRX" onclick="window.location.href='/home'">
    <button onclick="window.location.href='/employees/view/all/list'"><span class="account"><img
            src="/static/logo/icons/employees.png" alt="Employees"><h6 style="color:white; margin-top: 7px;">Employees</h6></span>
    </button>
    <button onclick="window.location.href='/employees/view/all/tree'"><span class="account"><img
            src="/static/logo/icons/hierarchy.png" alt="Hierarchy"><h6 style="color:white; margin-top: 7px;">Hierarchy</h6></span>
    </button>
    <button onclick="window.location.href='/employees/view/{{ account.ID }}'"><span class="account"><img
            src="/static/logo/o-white.png" alt="My Account"><h6 style="color:white; margin-top: 7px;">My account</h6></span>
    </button>
    <button onclick="window.location.href='/settings/account'"><span class="account"><img
            src="/static/logo/icons/logout.png" alt="Log out"><h6 style="color:white; margin-top: 7px;">Log Out</h6></span>
    </button>"""

headerlogin = """
    <img src="/static/logo/oopenhrx-white.png" alt="(8)OpenHRX" onclick="window.location.href='/home'">
    <button onclick="window.location.href='/login'"><span class="account"><img
            src="/static/logo/o-white.png" alt="Login"><h6 style="color:white; margin-top: 7px;">Login</h6></span>
    </button>"""

