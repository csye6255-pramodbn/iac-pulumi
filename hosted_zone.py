from pulumi_aws import route53
from instance import *
from variables import *

public_ip = public_ips
hosted_zone = route53.get_zone(name=zone_name)

# DNS record function to create or update the A records
def manage_dns_record(subdomain, zone_name, hosted_zone_id, record_type, ttl, ips):
    for ip in ips:
        record_fqdn = f"{subdomain}.{zone_name}" if subdomain else zone_name
        return route53.Record(record_fqdn,
                          zone_id=hosted_zone_id,
                          name=record_fqdn,
                          type=record_type,
                          ttl=ttl,
                          records=[ip])

# Uses the manage_dns_record function to create or update the A records
demo_record = manage_dns_record('', zone_name, hosted_zone.id, A_record, ttl, public_ip)
www_record = manage_dns_record('www', zone_name, hosted_zone.id, A_record, ttl, public_ip)