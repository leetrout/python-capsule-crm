python-capsule-crm
==================

Python wrapper for Capsule CRM API.

Currently in development- read only.


Installing
==========

`pip install capsule_crm`

Dependencies
------------

Requires [Requests](http://docs.python-requests.org/en/latest/).


Config
======

You'll need your api key and account subdomain name.

You may provide these parameters in your code or with the environment variables
`CAPSULE_NAME` &amp; `CAPSULE_KEY`


Usage
=====

#### Instantiate ####

First, instantiate the API wrapper object

    from capsule_crm import CapsuleCRM
    cap = CapsuleCRM(cap_name="foo", cap_key="XXXYYYZZZ")

Or if you have configured the environment variables, simply

    from capsule_crm import CapsuleCRM
    cap = CapsuleCRM()

#### Define request ####

Defining a request is simply chaining a method to the API wrapper instance

    parties = cap.party()

That will return a new wrapper object representing a request to list all parties.

#### Retrieve results ####

We can retrieve the parsed JSON results easily by using the json property

    results = parties.json

All of this could also be written more concisely as

    cap.party().json

#### Using URL paramters ####

Using URL parameters is easy-just pass them as arguments to the endpoint's method.

Consider the endpoint /api/party/:party-id

    cap.party('12345')

Or /api/party/:id/people

    cap.party('12345').people()

#### Using query string parameters ####

Of course adding query string parameters to a GET request is easy- just pass them as keyword arguments
to the method. For example, to filter the parties

    cap.party(q="Bob")

For any other method (POST, PUT, etc) the keyword arguments will become the request
body. If you need to set a querystring on those request methods use the `set_qs()` method.

For example, to assign a track when creating an opportunity:

    resp = cap.party('12345').opportunity(
        opportunity={'name':'Awesome Opp'}
    ).set_qs({'trackId':'123456'}).post()




TODO
====

 + Test with task creation
 + Add full examples to this readme
 + Add tests

