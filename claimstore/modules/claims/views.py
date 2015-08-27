# -*- coding: utf-8 -*-
#
# This file is part of ClaimStore.
# Copyright (C) 2015 CERN.
#
# ClaimStore is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# ClaimStore is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ClaimStore; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307,
# USA.

"""ClaimStore views."""

from flask import Blueprint, render_template

from claimstore.core.json import get_json_schema

blueprint = Blueprint(
    'claims_views',
    __name__,
)


@blueprint.route('/', methods=['GET'])
def index():
    """Render the home page for ClaimStore."""
    return render_template('cover.html', active_menu='home')


@blueprint.route('/subscription', methods=['GET'])
def subscription():
    """Render the subscription form page."""
    return render_template(
        "subscription.html",
        json_schema=get_json_schema('claims.claimant')
    )


@blueprint.route('/api', methods=['GET'])
def api():
    """Render the api documenation page."""
    return render_template("api.html", active_menu='api')


@blueprint.route('/contact', methods=['GET'])
def contact():
    """Render the contact page."""
    return render_template("contact.html", active_menu='contact')
