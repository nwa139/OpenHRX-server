#                     OpenHRX:  Free and Open Source EMS
#                      Copyright (C) 2025-2026  OpenHRX
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License as published
#     by the Free Software Foundation, either version 3 of the License, or
#     any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.
#
#     You should have received a copy of the GNU Affero General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

from flask import Flask, render_template
import queries as q
import html
app = Flask(__name__)

localAccount = {"ID": None, "saveLogin": False}
local = { "footer": html.footer, "header": html.header, "headerlogin": html.headerlogin}

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", local=local, account=localAccount)

@app.route("/code", methods=["GET"])
def code():
    return render_template("code.html", local=local, account=localAccount)

@app.route("/legal", methods=["GET"])
def legal():
    return render_template("legal.html", local=local, account=localAccount)

#List all Employees on DB (List View)
@app.route("/employees/view/all/list", methods=["GET"])
def employees_view_all():
    db_status = q.ensure_db()
    if db_status is not True:
        return render_template("error.html", local=local, account=localAccount,error=str(db_status))
    EmployeesList = q.get_employees()

    return render_template("employees.html", local=local, account=localAccount, employees=EmployeesList)

#Individual View (View Only)
@app.route("/employees/view/<urlid>", methods=["GET"])
def employee_view(urlid):
    db_status = q.ensure_db()
    if db_status is not True:
        return render_template("error.html", local=local, account=localAccount, error=str(db_status), )
    employee_id = urlid.upper()
    employee = q.get_employee(employee_id)
    if employee:
        return render_template("employeeviewer.html", local=local, account=localAccount, employee=employee)
    else:
        return render_template("error.html", local=local, account=localAccount, error=f"Employee with ID {{{employee_id}}} not found in database {q.database}@{q.host}:{q.port}")

# Account Settings (NYI)
@app.route("/settings/account", methods=["GET"])
def settings_account():
    return render_template("base.html", local=local, account=localAccount)

if __name__ == "__main__":
    app.run(debug=True)
