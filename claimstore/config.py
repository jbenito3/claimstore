# -*- coding: utf-8 -*-
#
# This file is part of ClaimStore.
# Copyright (C) 2015 CERN.
#
# ClaimStore is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
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

"""ClaimStore configuration."""

import os

# -----------------------------------------------------------------------------
# GENERAL CONFIG
# -----------------------------------------------------------------------------

# Base directory
BASE_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
if 'CLAIMSTORE_DEBUG' in os.environ:
    CLAIMSTORE_DEBUG = os.environ['CLAIMSTORE_DEBUG'] == 'True'
else:
    CLAIMSTORE_DEBUG = False
if 'CLAIMSTORE_HOST' in os.environ:
    CLAIMSTORE_HOST = os.environ['CLAIMSTORE_HOST']
else:
    CLAIMSTORE_HOST = '0.0.0.0'
if 'CLAIMSTORE_PORT' in os.environ:
    CLAIMSTORE_PORT = int(os.environ['CLAIMSTORE_PORT'])
else:
    CLAIMSTORE_PORT = 5000


# -----------------------------------------------------------------------------
# DATABASE
# -----------------------------------------------------------------------------

# Define the database as environment variable
if 'SQLALCHEMY_DATABASE_URI' in os.environ:
    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']


# -----------------------------------------------------------------------------
# SECURITY
# -----------------------------------------------------------------------------

# Define the IP networks (e.g. 146.16.0.0/16) that can use the RESTful API.
# The list of IP networks should be separated by whitespaces.
if 'CLAIMSTORE_ALLOWED_IPS' in os.environ and \
        os.environ['CLAIMSTORE_ALLOWED_IPS'].strip():
    CLAIMSTORE_ALLOWED_IPS = os.environ['CLAIMSTORE_ALLOWED_IPS'].split(' ')
else:
    CLAIMSTORE_ALLOWED_IPS = ['0.0.0.0/0']


# -----------------------------------------------------------------------------
# CLAIMS
# -----------------------------------------------------------------------------

CFG_EQUIVALENT_PREDICATES = ['is_same_as', 'is_variant_of']
CFG_PAGINATION_ARG_PAGE = 1
CFG_PAGINATION_ARG_PER_PAGE = 20
