import http.client




def newHTTPResponse(url, status=200, headers={}, body=b"", reason="ok"):

  def response():
    pass

  response.url = f"{url}"

  def geturl():
    return url

  response.geturl = geturl
  response.status = status

  def getcode():
    return status

  response.getcode = getcode
  response.headers = headers

  def getheaders():
    return list(response.headers.items())

  response.getheaders = getheaders

  def info():
    return response.headers

  response.info = info

  def getheader(name, default=None):
    try:
      return response.headers[name]
    except:
      return default

  response.getheader = getheader
  response.body = body

  def read(amt=len(response.body)):
    return response.body[0:amt]

  response.read = read

  def readinto(b):
    return response.body[0:len(b)]

  response.readinto = readinto
  response.reason = reason
  response.debuglevel = 0
  response.closed = True
  response.msg = headers
  response.version = "HTTP/1.1"
  return response


def fetch(url, options={}):
    url = f"{url}"
    method = 'GET'
    if ('method' in options.keys()):
      method = f"{options['method']}".upper()
    body = None
    if ('body' in options.keys()):
      body = options['body']
    headers = {}
    if ('headers' in options.keys()):
      headers = options['headers']
    host = url.split('/')[2]
    path = host.join(url.split(host)[1:])
    print(path)
    connection = http.client.HTTPSConnection(host)
    connection.request(method, path, body=body, headers=headers)
    response = connection.getresponse()
    if not hasattr(response,'url'):
      setattr(response,'url',url)
    if not hasattr(response,'geturl'):
      def geturl():
        return url
      response.geturl = geturl
    if not hasattr(response,'info'):
      def info():
        return response.headers
      response.info = info
    if not hasattr(response,'getcode'):
      def getcode():
        return response.status
      response.getcode = getcode
    return response

def zfetch(url, options={}):
  res = {}
  try:
    res = fetch(url,options=options)
  except Exception as e:
    res = newHTTPResponse(url, status=569, body=b(f"{e}"), reason=f"{e}")
  def zread(amt=None):
    try:
      return res.read(amt=amt)
    except Exception as e:
      return b(f"{e}")
  res.zread = zread
  return res