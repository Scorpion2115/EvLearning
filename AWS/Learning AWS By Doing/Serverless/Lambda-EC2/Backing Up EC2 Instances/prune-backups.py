import boto3


def lambda_handler(event, context):
    # grab the account ID
    account_id = boto3.client('sts').get_caller_identity().get('Account')
    ec2 = boto3.client('ec2')
    regions = [region['RegionName']
               for region in ec2.describe_regions()['Regions']]

    for region in regions:
        print("Region:", region)
        ec2 = boto3.client('ec2', region_name=region)
        response = ec2.describe_snapshots(OwnerIds=[account_id])
        snapshots = response["Snapshots"]

        # Sort snapshots by date ascending
        snapshots.sort(key=lambda x: x["StartTime"])

        # Remove snapshots we want to keep (i.e. 3 most recent)
        snapshots = snapshots[:-3]

        for snapshot in snapshots:
            id = snapshot['SnapshotId']
            try:
                # describe the snapshot associate with my account ID only
                print("Deleting snapshot:", id)
                ec2.delete_snapshot(SnapshotId=id)
            # skip the deletion process, if the snapshot is currently in use    
            except Exception as e:
                print("Snapshot {} in use, skipping.".format(id))
                continue