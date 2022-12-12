
token = ''
webhook = False
WEBHOOK_HOST = ''
WEBHOOK_PORT = 8443  # 443, 80, 88 or 8443 (port need to be 'open')
WEBHOOK_LISTEN = '217.163.29.237'  # In some VPS you may need to put here the IP addr

WEBHOOK_SSL_CERT = ''  # Path to the ssl certificate
WEBHOOK_SSL_PRIV = ''  # Path to the ssl private key
WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (token)
