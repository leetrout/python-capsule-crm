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

#### Using query string parameters ####

Of course adding query string parameters is easy- just pass them as keyword arguments
to the method. For example, to filter the parties

    cap.party(q="Bob")

#### Using URL paramters ####

Using URL parameters is also easy-just pass them as arguments to the endpoint's method.

Consider the endpoint /api/party/:party-id

    cap.party('12345')

Or /api/party/:id/people

    cap.party('12345').people()


TODO
====

 + Test with task creation
 + Add full examples to this readme
 + Add tests

