from loguru import logger
from githubhosts.ali import AliPing
from githubhosts.utils import ip_ping, write_hosts

HOSTS = [
    "github.githubassets.com",
    "central.github.com",
    "desktop.githubusercontent.com",
    "assets-cdn.github.com",
    "camo.githubusercontent.com",
    "github.map.fastly.net",
    "github.global.ssl.fastly.net",
    "gist.github.com",
    "github.io",
    "github.com",
    "api.github.com",
    "raw.githubusercontent.com",
    "user-images.githubusercontent.com",
    "favicons.githubusercontent.com",
    "avatars5.githubusercontent.com",
    "avatars4.githubusercontent.com",
    "avatars3.githubusercontent.com",
    "avatars2.githubusercontent.com",
    "avatars1.githubusercontent.com",
    "avatars0.githubusercontent.com",
    "avatars.githubusercontent.com",
    "codeload.github.com",
    "github-cloud.s3.amazonaws.com",
    "github-com.s3.amazonaws.com",
    "github-production-release-asset-2e65be.s3.amazonaws.com",
    "github-production-user-asset-6210df.s3.amazonaws.com",
    "github-production-repository-file-5c1aeb.s3.amazonaws.com",
    "githubstatus.com",
    "github.community",
    "media.githubusercontent.com",
    "objects.githubusercontent.com",
    "raw.github.com",
    "copilot-proxy.githubusercontent.com",
]

if __name__ == "__main__":
    host_ips = []
    for host in HOSTS:
        ips = list(set(AliPing().get_all_ip(host)))
        logger.info(f"Get {len(ips)} ip from ali in {host}")
        valid_ips = []
        for ip in ips:
            e = ip_ping(ip)
            if e >= 0:
                logger.info(f"Test {ip} for {host} pass deplay {e}ms")
                valid_ips.append((ip, e))
            else:
                logger.info(f"Test {ip} for {host} not pass")
        if valid_ips:
            sorted_ips = sorted(valid_ips, key=lambda x: x[1])
            ip = sorted_ips[0][0]
            host_ips.append((ip, host))
    write_hosts(host_ips)
