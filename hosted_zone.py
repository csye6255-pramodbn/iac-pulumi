from pulumi_aws import route53
from variables import *
from load_balancer import *

hosted_zone = route53.get_zone(name=zone_name)


# Create an Alias A record pointing to an AWS resource like an ALB
def manage_alias_dns_record(subdomain, zone_name, hosted_zone_id, alb_target_zone_id, alb_dns_name):
    record_fqdn = f"{subdomain}.{zone_name}" if subdomain else zone_name
    return route53.Record(record_fqdn,
                          zone_id=hosted_zone_id, # Hosted Zone ID
                          name=record_fqdn,
                          type="A",
                          aliases=[{
                              "name": alb_dns_name,
                              "zone_id": alb_target_zone_id, # AZ id of the ALB
                              "evaluate_target_health": alb_evaluate_target_health, # true
                          }])

# Uses the manage_dns_record function to create or update the A records
sub_record = manage_alias_dns_record('', zone_name, hosted_zone.id, alb_target_zone_id, alb_dns_name)
www_record = manage_alias_dns_record('www', zone_name, hosted_zone.id, alb_target_zone_id, alb_dns_name)