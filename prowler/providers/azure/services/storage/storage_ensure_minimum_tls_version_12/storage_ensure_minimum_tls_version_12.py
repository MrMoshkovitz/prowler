from prowler.lib.check.models import Check, Check_Report
from prowler.providers.azure.services.storage.storage_client import storage_client


class storage_ensure_minimum_tls_version_12(Check):
    def execute(self) -> Check_Report:
        findings = []
        for subscription, storage_accounts in storage_client.storage_accounts.items():
            for storage_account in storage_accounts:
                report = Check_Report(self.metadata())
                report.region = storage_client.region
                report.status = "PASS"
                report.status_extended = f"Storage account {storage_account.name} from subscription {subscription} has TLS version set to 1.2"
                report.resource_id = storage_account.name
                report.resource_arn = storage_account.id
                if storage_account.minimum_tls_version != "TLS1_2":
                    report.status = "FAIL"
                    report.status_extended = f"Storage account {storage_account.name} from subscription {subscription} does not have TLS version set to 1.2"

                findings.append(report)

        return findings