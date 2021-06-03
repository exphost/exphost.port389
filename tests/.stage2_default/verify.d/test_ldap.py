def test_user_credentials(host):
    assert host.run("ldapwhoami -D uid=testuser,ou=People,dc=test-0,dc=localdomain -w testuserpass -x").rc == 0

def test_user_credentials_wrong_pass(host):
    assert host.run("ldapwhoami -D uid=testuser,ou=People,dc=test-0,dc=localdomain -w tsd123 -x").rc != 0
def test_user_credentials_unknow_user(host):
    assert host.run("ldapwhoami -D uid=testuser2,ou=People,dc=test-0,dc=localdomain -w testuserpass -x").rc != 0
