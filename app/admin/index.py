from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app

admin = Blueprint('admin', __name__, url_prefix='/')

@admin.route('/admin', methods=['GET'])
def index():
    return render_template('/admin/index.html')

@admin.route('/member', methods=['GET'])
def member():
    return render_template('/admin/tables.html')
