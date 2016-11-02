from JumpScale import j

from IPython import embed
print("DEBUG NOW 999")
embed()
raise RuntimeError("stop debug here")

from bravado.client import SwaggerClient
client = SwaggerClient.from_url('file://spec.json')

from IPython import embed
print("DEBUG NOW pp")
embed()
raise RuntimeError("stop debug here")
