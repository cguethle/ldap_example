"""
Short ldap example...

Test ldap server is...

Server: ldap.forumsys.com  
Port: 389

Bind DN: cn=read-only-admin,dc=example,dc=com
Bind Password: password

All user passwords are password.

You may also bind to individual Users (uid) or the two Groups (ou) that include:

ou=mathematicians,dc=example,dc=com

riemann
gauss
euler
euclid

ou=scientists,dc=example,dc=com

einstein
newton
galieleo
tesla

For more details see http://www.forumsys.com/en/tutorials/integration-how-to/ldap/online-ldap-test-server/
Thanks for the free server!!!
"""
import ldap
import json

LDAP_SERVER = 'ldap.forumsys.com'

DN_READONLY_ADMIN = 'cn=read-only-admin,dc=example,dc=com'

DN_MATHEMATICIANS = 'ou=mathematicians,dc=example,dc=com'
DN_SCIENTISTS = 'ou=scientists,dc=example,dc=com'

DN_TESLA = 'uid=tesla,{parent_dn}'.format(parent_dn=DN_SCIENTISTS)
DN_EINSTEIN = 'uid=einstein,dc=example,dc=com'

try:
  conn = ldap.initialize('ldap://{server_url}'.format(server_url=LDAP_SERVER))
  ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_ALLOW)	# allow self signed for this test server.
  conn.start_tls_s()
  print conn.bind_s(DN_READONLY_ADMIN, 'password')
  print "I am connected as {dn}".format(dn=conn.whoami_s())
  print json.dumps(conn.search_s( DN_SCIENTISTS, ldap.SCOPE_SUBTREE, '(objectclass=*)', ['*'] ), indent=4)
finally:
  conn.unbind()
