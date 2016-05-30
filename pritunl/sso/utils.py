from pritunl import settings
from pritunl import plugins

def plugin_sso_authenticate(sso_type, user_name, remote_ip):
    from pritunl import organization

    returns = plugins.caller(
        'sso_authenticate',
        sso_type=sso_type,
        host_id=settings.local.host_id,
        host_name=settings.local.host.name,
        user_name=user_name,
        remote_ip=remote_ip,
    )

    if not returns:
        return True, None

    org_name = None
    for return_val in returns:
        if not return_val[0]:
            return False, None
        if return_val[1]:
            org_name = return_val[1]

    org_id = None
    if org_name:
        org = organization.get_by_name(org_name, fields=('_id'))
        if org:
            org_id = org.id

    return True, org_id
