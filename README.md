Juju Charm Layers Index
=======================

This repo is the index of layers available for building Juju Charms.

Each layer is represented by a small JSON file in either the [`layers`](layers)
or [`interfaces`](interfaces) directory, depending on the type of layer, and
each file should conform to the schema encoded in the [`schema.json`](schema.json)
file.  Specifically, it must contain at least the following fields:

* `id`: The name by which the layer will be referenced in `layer.yaml`, e.g., `basic`
* `name`: The human-friendly name of the layer
* `repo`: The URL of the git or bzr repo for the layer
* `summary`: A short description of the purpose of the layer

The file can also contain a `docs` field, which can specify a link to documentation
for the layer.  If not specified, a link to a `README.md` file will be generated,
if the repo is hosted on GitHub or Launchpad, or the link to the repo will be used.

The name of the file must match the ID field, with a `.json` suffix.

To add or modify a layer in the index, just create a PR against this repo in
which you have added the appropriate JSON file and run the
[`update_readme.py`](update_readme.py) script to update the index below.

If you would like to build a charm using a fork of this repo (e.g., to test a
new layer before submitting a PR, if you have private layers or layers under
test and don't want to use [local layers][local], etc.), you just need to pass
in a URL where the repo contents are available via HTTP/S to `charm-build`.
For example, to build using a fork in your personal namespace in GitHub:

```
charm build --interface-service https://raw.githubusercontent.com/myuser/layer-index/mybranch/
```

[local]: https://github.com/juju/charm-tools/blob/master/doc/source/build.md#setting-up-your-repo



List of Base Layers
===================

<!-- list-of-layers -->

| ID | Repo | Docs | Name | Summary |
| --- | --- | --- | --- | --- |
| ansible-base | [Repo](https://github.com/chuckbutler/ansible-base) | [Docs](https://github.com/chuckbutler/ansible-base#readme) | ansible-base | Base / charm layer for charming w/ Ansible |
| apache-bigtop-base | [Repo](https://github.com/juju-solutions/layer-apache-bigtop-base.git) | [Docs](https://github.com/juju-solutions/layer-apache-bigtop-base.git#readme) | Apache Bigtop Base Layer | Base layer for charms needing Apache Bigtop  |
| apache-bigtop-gateway | [Repo](https://github.com/juju-solutions/layer-apache-bigtop-gateway) | [Docs](https://github.com/juju-solutions/layer-apache-bigtop-gateway#readme) | apache-bigtop-gateway | Base layer for Gateway node from Apache Big Top |
| apache-flume-base | [Repo](https://github.com/juju-solutions/layer-apache-flume-base.git) | [Docs](https://github.com/juju-solutions/layer-apache-flume-base.git#readme) | Apache Flume Base | Base layer for Apache Flume charms |
| apache-hadoop-datanode | [Repo](https://github.com/juju-solutions/layer-apache-hadoop-datanode.git) | [Docs](https://github.com/juju-solutions/layer-apache-hadoop-datanode.git#readme) | Apache Hadoop DataNode | Base / charm layer for the DataNode component of Hadoop |
| apache-hadoop-namenode | [Repo](https://github.com/juju-solutions/layer-apache-hadoop-namenode.git) | [Docs](https://github.com/juju-solutions/layer-apache-hadoop-namenode.git#readme) | Apache Hadoop NameNode | Charm layer for the NameNode component of Hadoop |
| apache-hadoop-nodemanager | [Repo](https://github.com/juju-solutions/layer-apache-hadoop-nodemanager.git) | [Docs](https://github.com/juju-solutions/layer-apache-hadoop-nodemanager.git#readme) | Apache Hadoop NodeManager | Base / charm layer for the NodeManager component of Hadoop |
| apache-hadoop-plugin | [Repo](https://github.com/juju-solutions/layer-apache-hadoop-plugin.git) | [Docs](https://github.com/juju-solutions/layer-apache-hadoop-plugin.git#readme) | apache-hadoop-plugin | Simplified connection point for Apache Hadoop platform |
| apache-hadoop-resourcemanager | [Repo](https://github.com/juju-solutions/layer-apache-hadoop-resourcemanager.git) | [Docs](https://github.com/juju-solutions/layer-apache-hadoop-resourcemanager.git#readme) | Apache Hadoop ResourceManager | Charm layer for the ResourceManager component of Hadoop |
| apache-hadoop-slave | [Repo](https://github.com/juju-solutions/layer-apache-hadoop-slave.git) | [Docs](https://github.com/juju-solutions/layer-apache-hadoop-slave.git#readme) | apache-hadoop-slave | Combined slave node (DataNode + NodeManager) for Apache Hadoop |
| apache-php | [Repo](https://github.com/juju-solutions/layer-apache-php.git) | [Docs](https://github.com/juju-solutions/layer-apache-php.git#readme) | Apache PHP base layer | Configurable base for Apache PHP charms |
| apache-wsgi | [Repo](https://git.launchpad.net/~jacekn/charms/+source/apache-wsgi) | [Docs](https://git.launchpad.net/~jacekn/charms/+source/tree/README.md) | Apache WSGI base layer | Configurable base for Apache WSGI charms |
| apt | [Repo](https://git.launchpad.net/layer-apt) | [Docs](https://github.com/stub42/layer-apt#readme) | Apt layer | Easily deal with apt sources and deb packages |
| barbican-client | [Repo](https://github.com/omnivector-solutions/layer-barbican-client) | [Docs](https://github.com/omnivector-solutions/layer-barbican-client#readme) | Barbican Client | Reactive layer to help pull secrets from barbican |
| basic | [Repo](https://github.com/juju-solutions/layer-basic.git) | [Docs](https://github.com/juju-solutions/layer-basic.git#readme) | Basic Layer | Base layer for charms with the Reactive framework |
| beats-base | [Repo](https://github.com/juju-solutions/layer-beats-base) | [Docs](https://github.com/juju-solutions/layer-beats-base#readme) | Beats Base | Base layer for Elastic Beats |
| bigtop-base | [Repo](https://github.com/juju-solutions/layer-apache-bigtop-base.git) | [Docs](https://github.com/juju-solutions/layer-apache-bigtop-base.git#readme) | Apache Bigtop Base Layer | Base layer for charms needing Apache Bigtop  |
| buildpacks | [Repo](https://git.launchpad.net/~bcsaller/charms/+source/buildpacks) | [Docs](https://git.launchpad.net/~bcsaller/charms/+source/tree/README.md) | Buildpacks | Experimental layer for using buildpacks to generate Charmed applications |
| caas-base | [Repo](https://github.com/juju-solutions/layer-caas-base.git) | [Docs](https://github.com/juju-solutions/layer-caas-base.git#readme) | Base Layer for CAAS charms | Base layer for CAAS charms with the Reactive framework |
| cdk-service-kicker | [Repo](https://github.com/juju-solutions/layer-cdk-service-kicker.git) | [Docs](https://github.com/juju-solutions/layer-cdk-service-kicker.git#readme) | CDK Service Kicker | Installs a background service, cdk-service-kicker, for kicking cdk services. |
| ceph-base | [Repo](https://github.com/ChrisMacNaughton/layer-ceph-base) | [Docs](https://github.com/ChrisMacNaughton/layer-ceph-base#readme) | EXPERIMENTAL Ceph Base Layer | EXPERIMENTAL Ceph base layer |
| ceph-basic | [Repo](https://github.com/ChrisMacNaughton/layer-ceph-basic) | [Docs](https://github.com/ChrisMacNaughton/layer-ceph-basic#readme) | EXPERIMENTAL ceph-basic | EXPERIMENTAL ceph-basic layer |
| ceph-mon | [Repo](https://github.com/ChrisMacNaughton/juju-layer-ceph-mon) | [Docs](https://github.com/ChrisMacNaughton/juju-layer-ceph-mon#readme) | EXPERIMENTAL Ceph Mon layer | EXPERIMENTAL Ceph Mon layer |
| ceph | [Repo](https://github.com/openstack/charm-layer-ceph.git) | [Docs](https://github.com/openstack/charm-layer-ceph.git#readme) | Ceph Layer | Ceph base layer |
| charmscaler-base | [Repo](https://github.com/elastisys/layer-charmscaler-base) | [Docs](https://github.com/elastisys/layer-charmscaler-base#readme) | Charmscaler Base | Charmscaler base layer |
| cis-benchmark | [Repo](https://github.com/charmed-kubernetes/layer-cis-benchmark) | [Docs](https://github.com/charmed-kubernetes/layer-cis-benchmark#readme) | CIS Benchmark base layer | Provides a cis-benchmark action for the CIS Kubernetes benchmark. |
| conda-api | [Repo](https://github.com/omnivector-solutions/layer-conda-api) | [Docs](https://github.com/omnivector-solutions/layer-conda-api#readme) | Conda API | Conda API layer |
| consul-base | [Repo](https://github.com/omnivector-solutions/layer-consul-base) | [Docs](https://github.com/omnivector-solutions/layer-consul-base#readme) | Consul Base | Reactive base layer for consul |
| container-runtime-common | [Repo](https://github.com/charmed-kubernetes/layer-container-runtime-common.git) | [Docs](https://github.com/charmed-kubernetes/layer-container-runtime-common.git#readme) | Container Runtime Common | Shared between container runtimes |
| coordinator | [Repo](https://git.launchpad.net/layer-coordinator ) | [Docs](https://git.launchpad.net/layer-coordinator/tree/README.md) | Coordinator Layer | Coordinate operations between units in a service, such as rolling restarts. |
| debug | [Repo](https://github.com/juju-solutions/layer-debug.git) | [Docs](https://github.com/juju-solutions/layer-debug.git#readme) | debug | Provides a troubleshooting debug action |
| django | [Repo](https://github.com/marcoceppi/layer-django.git) | [Docs](https://github.com/marcoceppi/layer-django.git#readme) | Django | Django / GUNICORN |
| docker-resource | [Repo](https://github.com/juju-solutions/layer-docker-resource.git) | [Docs](https://github.com/juju-solutions/layer-docker-resource.git#readme) | Docker Resource Layer | Layer for managing charm resources of type 'docker' |
| docker | [Repo](https://github.com/juju-solutions/layer-docker.git) | [Docs](https://github.com/juju-solutions/layer-docker.git#readme) | Docker | Layer to deliver and install Docker on Ubuntu, Debian, Centos hosts. |
| elastic-base | [Repo](https://github.com/omnivector-solutions/layer-elastic-base.git) | [Docs](https://github.com/omnivector-solutions/layer-elastic-base.git#readme) | Elastic-Base | Base layer for Elastic.co charms |
| elasticsearch-client | [Repo](https://github.com/omnivector-solutions/layer-elasticsearch-client) | [Docs](https://github.com/omnivector-solutions/layer-elasticsearch-client#readme) | Elasticsearch Client | Elasticsearch client layer |
| elixir | [Repo](https://github.com/battlemidget/juju-layer-elixir.git) | [Docs](https://github.com/battlemidget/juju-layer-elixir.git#readme) | Elixir | Runtime layer for Elixir applications |
| flannel | [Repo](https://github.com/juju-solutions/layer-flannel) | [Docs](https://github.com/juju-solutions/layer-flannel#readme) | Flannel | Flannel Overlay Network layer for docker |
| flask | [Repo](https://github.com/tengu-team/layer-flask) | [Docs](https://github.com/tengu-team/layer-flask#readme) | Flask | Layer to create Flask webservers running on nginx |
| git-deploy | [Repo](https://github.com/omnivector-solutions/layer-git-deploy.git) | [Docs](https://github.com/omnivector-solutions/layer-git-deploy.git#readme) | Git Deploy | Layer to aid with deploying code from github |
| go-binary | [Repo](https://github.com/cloud-green/go-binary-layer) | [Docs](https://github.com/cloud-green/go-binary-layer#readme) | Go Binary Base Layer | Takes a statically compiled go binary and starts it as a service |
| hacluster | [Repo](https://github.com/juju-solutions/layer-hacluster.git) | [Docs](https://github.com/juju-solutions/layer-hacluster.git#readme) | Hacluster | Layer that provides hacluster for high availability |
| hadoop-base | [Repo](https://github.com/juju-solutions/layer-hadoop-base.git) | [Docs](https://github.com/juju-solutions/layer-hadoop-base.git#readme) | Hadoop Base | Base layer for a charm needing the Apache Hadoop libraries |
| hadoop-client | [Repo](https://github.com/juju-solutions/layer-hadoop-client.git) | [Docs](https://github.com/juju-solutions/layer-hadoop-client.git#readme) | hadoop-client | Base and charm layer for Hadoop clients |
| hadoop-datanode | [Repo](https://github.com/juju-solutions/layer-hadoop-datanode) | [Docs](https://github.com/juju-solutions/layer-hadoop-datanode#readme) | hadoop-datanode | Base layer for DataNode from Apache BigTop |
| hadoop-ganglia | [Repo](https://github.com/juju-solutions/layer-hadoop-ganglia.git) | [Docs](https://github.com/juju-solutions/layer-hadoop-ganglia.git#readme) | hadoop-ganglia | Base layer for adding Ganglia support to Hadoop core charms |
| hadoop-nodemanager | [Repo](https://github.com/juju-solutions/layer-hadoop-nodemanager) | [Docs](https://github.com/juju-solutions/layer-hadoop-nodemanager#readme) | hadoop-nodemanager | Base layer for NodeManager from Apache BigTop |
| haproxy-core | [Repo](https://github.com/juju-solutions/layer-haproxy-core.git) | [Docs](https://github.com/juju-solutions/layer-haproxy-core.git#readme) | haproxy-core | A reactive layer that delivers a minimal haproxy layer to use in other application layers. |
| hhvm | [Repo](https://github.com/battlemidget/juju-layer-hhvm) | [Docs](https://github.com/battlemidget/juju-layer-hhvm#readme) | HHVM | Provides HHVM and composer for php applications |
| ibm-base | [Repo](https://code.launchpad.net/~ibmcharmers/layer-ibm-base/trunk) | [Docs](https://bazaar.launchpad.net/~ibmcharmers/layer-ibm-base/files/README.md) | IBM Base Layer | Base layer for IBM charms |
| ibm-im | [Repo](http://launchpad.net/~ibmcharmers/ibmlayers/layer-ibm-im) | [Docs](http://bazaar.launchpad.net/~ibmcharmers/ibmlayers/files/README.md) | IBM IM | This layer provides IBM Installation Manager, which can be used to install many IBM products. |
| ibm-was-nd | [Repo](https://code.launchpad.net/~ibmcharmers/charms/trusty/layer-ibm-was-nd/trunk) | [Docs](https://bazaar.launchpad.net/~ibmcharmers/charms/trusty/layer-ibm-was-nd/files/README.md) | IBM WAS ND | Charm layer for IBM WAS ND DM and WAS ND Node charms |
| jenkins-workspace | [Repo](https://github.com/juju-solutions/layer-jenkins-workspace) | [Docs](https://github.com/juju-solutions/layer-jenkins-workspace#readme) | Jenkins Workspace | Configure Jenkins with workspace snapshots |
| jenkins | [Repo](https://github.com/jenkinsci/jenkins-charm.git) | [Docs](https://github.com/jenkinsci/jenkins-charm.git#readme) | jenkins | Juju charm to deploy and scale Jenkins  |
| juju-client | [Repo](https://github.com/tengu-team/layer-juju-client.git) | [Docs](https://github.com/tengu-team/layer-juju-client.git#readme) | juju-client | Layer for Charms which depend on Juju CLI being installed in active Model  |
| kubernetes-common | [Repo](https://github.com/charmed-kubernetes/layer-kubernetes-common) | [Docs](https://github.com/charmed-kubernetes/layer-kubernetes-common#readme) | Kubernetes common lib | Provides a common library for Kubernetes charms. |
| kubernetes-master-worker-base | [Repo](https://github.com/charmed-kubernetes/layer-kubernetes-master-worker-base) | [Docs](https://github.com/charmed-kubernetes/layer-kubernetes-master-worker-base#readme) | kubernetes-master-worker-base | Base layer for kubernetes-master and kubernetes-worker. |
| layer-debug | [Repo](https://github.com/charms/layer-debug.git) | [Docs](https://github.com/charms/layer-debug.git#readme) | debug | Provides a troubleshooting debug action |
| leadership | [Repo](https://git.launchpad.net/layer-leadership) | [Docs](https://git.launchpad.net/tree/README.md) | Leadership layer | Help reactive framework charms deal with Juju leadership |
| lets-encrypt | [Repo](https://github.com/cmars/layer-lets-encrypt) | [Docs](https://github.com/cmars/layer-lets-encrypt#readme) | lets-encrypt | Automatic Let's Encrypt registration for Juju charms, just set the fqdn |
| Logrotate | [Repo](https://github.com/tbaumann/charm-layer-logrotate) | [Docs](https://github.com/tbaumann/charm-layer-logrotate#readme) | Logrotate layer | Logrotate layer to add logrotate entries in charms |
| lxd-proxy | [Repo](https://github.com/omnivector-solutions/layer-lxd-proxy) | [Docs](https://github.com/omnivector-solutions/layer-lxd-proxy#readme) | LXD Proxy | iptables proxy that adds and removes PREROUTING rules to ease host -> container proxying with juju |
| memcache-client | [Repo](https://github.com/omnivector-solutions/layer-memcache-client) | [Docs](https://github.com/omnivector-solutions/layer-memcache-client#readme) | Memcache Client | Client layer for Memcache |
| meter-status | [Repo](https://github.com/canonical/layer-meter-status) | [Docs](https://github.com/canonical/layer-meter-status#readme) | Meter Status Layer | Reactive charm layer supporting Juju meter status hooks |
| metrics | [Repo](https://github.com/canonical/layer-metrics) | [Docs](https://github.com/canonical/layer-metrics#readme) | Metrics Layer | Reactive charm layer supporting Juju metrics collection |
| munge | [Repo](https://github.com/omnivector-solutions/layer-munge) | [Docs](https://github.com/omnivector-solutions/layer-munge#readme) | munge | Reactive layer for Munge authentication service. |
| munin | [Repo](https://github.com/freyes/layer-munin) | [Docs](https://github.com/freyes/layer-munin#readme) | munin | munin server |
| nagios | [Repo](https://git.launchpad.net/nagios-layer) | [Docs](https://git.launchpad.net/tree/README.md) | Nagios Layer | Provide boilerplate required to relate services to the cs:nrpe subordinate |
| nginx-passenger | [Repo](https://github.com/omnivector-solutions/layer-nginx-passenger) | [Docs](https://github.com/omnivector-solutions/layer-nginx-passenger#readme) | Nginx Passenger | Reactive layer for nginx-passenger |
| nginx | [Repo](https://github.com/battlemidget/juju-layer-nginx.git) | [Docs](https://github.com/battlemidget/juju-layer-nginx.git#readme) | NGINX | NGINX layer for deploying web applications |
| nodejs | [Repo](https://github.com/battlemidget/juju-layer-node.git) | [Docs](https://github.com/battlemidget/juju-layer-node.git#readme) | NodeJS | Runtime layer for NodeJS applications |
| ntpmon | [Repo](https://git.launchpad.net/ntpmon) | [Docs](https://git.launchpad.net/tree/README.md) | ntpmon | NTP monitoring for telegraf |
| nvidia-cuda | [Repo](https://github.com/juju-solutions/layer-nvidia-cuda) | [Docs](https://github.com/juju-solutions/layer-nvidia-cuda#readme) | Nvidia CUDA | Installs CUDA and Nvidia drivers when supported GPU hardware is detected |
| openjdk | [Repo](https://github.com/juju-solutions/layer-openjdk.git) | [Docs](https://github.com/juju-solutions/layer-openjdk.git#readme) | OpenJDK | OpenJDK using the java layer |
| openstack-api | [Repo](https://github.com/openstack/charm-layer-openstack-api) | [Docs](https://github.com/openstack/charm-layer-openstack-api#readme) | OpenStack API layer | OpenStack API layer |
| openstack-principle | [Repo](https://github.com/openstack/charm-layer-openstack-principle) | [Docs](https://github.com/openstack/charm-layer-openstack-principle#readme) | OpenStack principle layer | OpenStack principle layer |
| openstack | [Repo](https://github.com/openstack/charm-layer-openstack) | [Docs](https://github.com/openstack/charm-layer-openstack#readme) | OpenStack base layer | OpenStack base layer |
| options | [Repo](https://github.com/juju-solutions/layer-options.git) | [Docs](https://github.com/juju-solutions/layer-options.git#readme) | options | Layer for reading options defined in layer.yaml |
| osm-ns | [Repo](https://github.com/charmed-osm/layer-osm-ns) | [Docs](https://github.com/charmed-osm/layer-osm-ns#readme) | osm-ns | A layer to build Open Source Mano (OSM) Network Service (NS) charms, to orchestrate the execution of actions across other charms within a model. |
| OVN | [Repo](https://github.com/openstack-charmers/charm-layer-ovn.git) | [Docs](https://github.com/openstack-charmers/charm-layer-ovn.git#readme) | OVN Layer | Base layer for Open Virtual Network Charms |
| promreg-client | [Repo](https://git.launchpad.net/~prometheus-registration-developers/prometheus-registration/+git/layer-promreg-client) | [Docs](https://git.launchpad.net/~prometheus-registration-developers/prometheus-registration/+git/tree/README.md) | promreg-client | A layer to aid in registering a target with Prometheus Registration |
| puppet-agent | [Repo](https://github.com/omnivector-solutions/layer-puppet-agent.git) | [Docs](https://github.com/omnivector-solutions/layer-puppet-agent.git#readme) | Puppet Agent | Puppet-agent layer - supports puppet 3 & 4. |
| puppet | [Repo](https://github.com/juju-solutions/layer-puppet.git) | [Docs](https://github.com/juju-solutions/layer-puppet.git#readme) | Puppet Layer (deprecated) | Puppet layer (deprecated; use puppet-agent) |
| ruby | [Repo](https://github.com/battlemidget/juju-layer-ruby.git) | [Docs](https://github.com/battlemidget/juju-layer-ruby.git#readme) | Ruby | Build layer for Ruby applications |
| slurm | [Repo](https://github.com/omnivector-solutions/layer-slurm) | [Docs](https://github.com/omnivector-solutions/layer-slurm#readme) | slurm | Base layer for Slurm |
| snap-action | [Repo](https://github.com/lutostag/layer-snap-action.git) | [Docs](https://github.com/lutostag/layer-snap-action.git#readme) | snap-action | Perform snap commands via an action |
| snap | [Repo](https://git.launchpad.net/layer-snap) | [Docs](https://git.launchpad.net/layer-snap/tree/README.md) | Snap layer | Snap layer for installing and updating Snap packages |
| sshproxy | [Repo](https://github.com/charmed-osm/layer-sshproxy) | [Docs](https://github.com/charmed-osm/layer-sshproxy#readme) | sshproxy | A layer intended to ease the development of charms that need to execute commands over SSH. |
| status | [Repo](https://github.com/juju-solutions/layer-status) | [Docs](https://github.com/juju-solutions/layer-status#readme) | Status management layer | Manage workload status in reactive charms |
| storage | [Repo](https://github.com/juju-solutions/layer-storage) | [Docs](https://github.com/juju-solutions/layer-storage#readme) | Storage | A charm layer to handle Juju attached storage devices. |
| supervisor | [Repo](https://github.com/omnivector-solutions/layer-supervisor) | [Docs](https://github.com/omnivector-solutions/layer-supervisor#readme) | Supervisor | Layer for Supervisor |
| swarm | [Repo](https://github.com/chuckbutler/layer-swarm.git) | [Docs](https://github.com/chuckbutler/layer-swarm.git#readme) | Docker Swarm | Stand alone layer, to extend docker into a Swarm cluster participant |
| tls-client | [Repo](https://github.com/juju-solutions/layer-tls-client.git) | [Docs](https://github.com/juju-solutions/layer-tls-client.git#readme) | tls-client | A layer to handle interface:tls-certificates requires side. |
| tls | [Repo](https://github.com/juju-solutions/layer-tls) | [Docs](https://github.com/juju-solutions/layer-tls#readme) | tls | The tls charm layer creates certificates and keys for each peer unit of a charm. |
| uwsgi | [Repo](https://github.com/marcoceppi/layer-uwsgi) | [Docs](https://github.com/marcoceppi/layer-uwsgi#readme) | uWSGI | uWSGI layer |
| vault-kv | [Repo](https://github.com/juju-solutions/layer-vault-kv) | [Docs](https://github.com/juju-solutions/layer-vault-kv#readme) | Vault KV layer | Layer for using Vault as a secure KV store |
| vaultlocker | [Repo](https://github.com/juju-solutions/layer-vaultlocker) | [Docs](https://github.com/juju-solutions/layer-vaultlocker#readme) | VaultLocker layer | Layer for managing secure disk storage locations using VaultLocker |
| venv | [Repo](https://github.com/omnivector-solutions/layer-venv.git) | [Docs](https://github.com/omnivector-solutions/layer-venv.git#readme) | venv | Layer for installing pip packages in a python3 venv |
| vnfproxy | [Repo](https://github.com/charmed-osm/vnfproxy.git) | [Docs](https://github.com/charmed-osm/vnfproxy.git#readme) | vnfproxy | A layer to ease development of "proxy" charms that operate against VNF images |

<!-- /list-of-layers -->

List of Interface Layers
========================

<!-- list-of-interfaces -->

| ID | Repo | Docs | Name | Summary |
| --- | --- | --- | --- | --- |
| ambassador | [Repo](https://github.com/juju-solutions/interface-ambassador.git) | [Docs](https://github.com/juju-solutions/interface-ambassador.git#readme) | ambassador | Interface layer for the Ambassador API Gateway |
| apache-website | [Repo](https://github.com/juju-solutions/interface-apache-website.git) | [Docs](https://github.com/juju-solutions/interface-apache-website.git#readme) | apache-website | Interface layer for the apache-website interface protocol |
| arangodb | [Repo](https://github.com/tengu-team/interface-arangodb.git) | [Docs](https://github.com/tengu-team/interface-arangodb.git#readme) | arangodb | Interface layer for ArangoDB |
| audit | [Repo](https://launchpad.net/~timkuhlman/charm-layer-auditd/audit-interface) | [Docs](https://bazaar.launchpad.net/~timkuhlman/charm-layer-auditd/files/README.md) | audit | Interface for use with the auditd charm |
| aws-elb | [Repo](https://github.com/omnivector-solutions/interface-aws-elb) | [Docs](https://github.com/omnivector-solutions/interface-aws-elb#readme) | AWS-ELB | AWS-ELB provides and requires interfaces. |
| aws-iam | [Repo](https://github.com/juju-solutions/interface-aws-iam) | [Docs](https://github.com/juju-solutions/interface-aws-iam#readme) | AWS-IAM | AWS-IAM interface for Kubernetes charm integration. |
| aws-integration | [Repo](https://github.com/juju-solutions/interface-aws-integration.git) | [Docs](https://github.com/juju-solutions/interface-aws-integration.git#readme) | aws-integration | Interface layer for connecting to the AWS integration charm |
| azure-integration | [Repo](https://github.com/juju-solutions/interface-azure-integration.git) | [Docs](https://github.com/juju-solutions/interface-azure-integration.git#readme) | azure-integration | Interface layer for connecting to the Azure integration charm |
| barbican-hsm | [Repo](https://opendev.org/x/charm-interface-barbican-hsm) | [Docs](https://opendev.org/x/charm-interface-barbican-hsm) | barbican-hsm | Interface supporting the integration between Barbican and HSM devices |
| barbican-secrets | [Repo](https://github.com/openstack/charm-interface-barbican-secrets.git) | [Docs](https://github.com/openstack/charm-interface-barbican-secrets.git#readme) | barbican-secrets | Interface supporting the integration between Barbican and secrets storage plugins |
| basic-auth-check | [Repo](https://github.com/CanonicalLtd/juju-interface-basic-auth-check) | [Docs](https://github.com/CanonicalLtd/juju-interface-basic-auth-check#readme) | basic-auth-check | Interface for the basic-auth-service to validate HTTP Basic-Auth credentials |
| benchmark | [Repo](https://github.com/juju-solutions/interface-benchmark.git) | [Docs](https://github.com/juju-solutions/interface-benchmark.git#readme) | benchmark | Interface layer for the benchmark protocol |
| bgp | [Repo](https://github.com/openstack/charm-interface-bgp.git) | [Docs](https://github.com/openstack/charm-interface-bgp.git#readme) | bgp | Interface layer for exchanging BGP neighbour information between charms |
| bind-client | [Repo](https://github.com/canonical/interface-bind-client) | [Docs](https://github.com/canonical/interface-bind-client#readme) | BIND CLIENT interface | BIND CLIENT interface |
| bind-rndc | [Repo](https://github.com/openstack/charm-interface-bind-rndc) | [Docs](https://github.com/openstack/charm-interface-bind-rndc#readme) | BIND RNDC interface | BIND RNDC interface |
| cassandra | [Repo](https://git.launchpad.net/interface-cassandra) | [Docs](https://git.launchpad.net/tree/README.md) | cassandra | Cassandra database client interface |
| ceph-admin | [Repo](https://github.com/openstack-charmers/juju-interface-ceph-admin) | [Docs](https://github.com/openstack-charmers/juju-interface-ceph-admin#readme) | ceph-admin | EXPERIMENTAL: The admin interface for ceph will provide the user with the ceph admin key |
| ceph-base | [Repo](https://github.com/openstack/charm-layer-ceph-base) | [Docs](https://github.com/openstack/charm-layer-ceph-base#readme) | Ceph Base Layer | Ceph base layer |
| ceph-client | [Repo](https://opendev.org/openstack/charm-interface-ceph-client.git) | [Docs](https://opendev.org/openstack/charm-interface-ceph-client/src/branch/master/src/ceph_client/README.md) | ceph-client | Ceph Client interface |
| ceph-mds | [Repo](https://opendev.org/openstack/charm-interface-ceph-client.git) | [Docs](https://opendev.org/openstack/charm-interface-ceph-client/src/branch/master/src/ceph_mds/README.md) | ceph-mds | CephFS interface to the MDS relation on ceph-mon |
| ceph-osd | [Repo](https://github.com/ChrisMacNaughton/juju-interface-ceph-osd) | [Docs](https://github.com/ChrisMacNaughton/juju-interface-ceph-osd#readme) | ceph-osd | ceph osd relation |
| ceph-radosgw | [Repo](https://github.com/ChrisMacNaughton/juju-interface-ceph-radosgw) | [Docs](https://github.com/ChrisMacNaughton/juju-interface-ceph-radosgw#readme) | ceph-radosgw | Ceph RadosGW interface |
| ceph-rbd-mirror | [Repo](https://github.com/openstack/charm-interface-ceph-rbd-mirror.git) | [Docs](https://github.com/openstack/charm-interface-ceph-rbd-mirror.git#readme) | ceph-rbd-mirror | Ceph RBD Mirror interface |
| ceph | [Repo](https://github.com/ChrisMacNaughton/juju-interface-ceph) | [Docs](https://github.com/ChrisMacNaughton/juju-interface-ceph#readme) | ceph | ceph mon peer interface |
| charms-ci | [Repo](https://github.com/juju-solutions/interface-charms-ci.git) | [Docs](https://github.com/juju-solutions/interface-charms-ci.git#readme) | charms-ci | Juju charms CI interface |
| cinder-backend | [Repo](https://github.com/openstack/charm-interface-cinder-backend.git) | [Docs](https://github.com/openstack/charm-interface-cinder-backend.git#readme) | cinder-backend | Interface for sending Cinder subordinate backend configuration to principle Cinder charms. |
| cinder-backup | [Repo](https://github.com/openstack/charm-interface-cinder-backup.git) | [Docs](https://github.com/openstack/charm-interface-cinder-backup.git#readme) | cinder-backup | Interface for sending Cinder-Backup external subordinate backend configuration. |
| cluster-dns | [Repo](https://github.com/charmed-kubernetes/interface-cluster-dns) | [Docs](https://github.com/charmed-kubernetes/interface-cluster-dns#readme) | cluster-dns | Cluster DNS Details for Charmed Kubernetes |
| conda | [Repo](https://github.com/omnivector-solutions/interface-conda) | [Docs](https://github.com/omnivector-solutions/interface-conda#readme) | Conda | Conda provides and requires interfaces |
| conn-check | [Repo](https://git.launchpad.net/~ubuntuone-hackers/conn-check/+git/interface-conn-check) | [Docs](https://git.launchpad.net/~ubuntuone-hackers/conn-check/+git/tree/README.md) | conn-check | conn-check interface |
| consul-agent | [Repo](https://github.com/ChrisMacNaughton/juju-interface-consul.git) | [Docs](https://github.com/ChrisMacNaughton/juju-interface-consul.git#readme) | consul-agent | Hashicorp Consul |
| consul | [Repo](https://github.com/juju-solutions/interface-consul) | [Docs](https://github.com/juju-solutions/interface-consul#readme) | consul | Hashicorp Consul |
| container-runtime | [Repo](https://github.com/charmed-kubernetes/interface-container-runtime.git) | [Docs](https://github.com/charmed-kubernetes/interface-container-runtime.git#readme) | Container Runtime | Interface for container runtimes |
| cwr-ci | [Repo](https://github.com/juju-solutions/interface-cwr-ci.git) | [Docs](https://github.com/juju-solutions/interface-cwr-ci.git#readme) | cwr-ci | Interface for relating to Cloud Weather Report (part of the Juju CI system) |
| dashboard-plugin | [Repo](https://github.com/openstack/charm-interface-dashboard-plugin.git) | [Docs](https://github.com/openstack/charm-interface-dashboard-plugin.git#readme) | dashboard-plugin | This interface is for use with OpenStack Dashboard plugin subordinate charms |
| db-info | [Repo](https://github.com/omnivector-solutions/interface-db-info) | [Docs](https://github.com/omnivector-solutions/interface-db-info#readme) | DB Info | Ease the process of application <-> application database creds transference. |
| db2 | [Repo](https://launchpad.net/~ibmcharmers/interface-ibm-db2/trunk) | [Docs](https://bazaar.launchpad.net/~ibmcharmers/interface-ibm-db2/files/README.md) | db2 | This interface layer handles the communication between  IBM DB2 and Consumer charms. |
| dbname | [Repo](https://github.com/omnivector-solutions/interface-dbname.git) | [Docs](https://github.com/omnivector-solutions/interface-dbname.git#readme) | DB Name | Interface to coordinate database name between applications. |
| designate | [Repo](https://github.com/openstack/charm-interface-designate) | [Docs](https://github.com/openstack/charm-interface-designate#readme) | designate | Designate DNS as a Service interface |
| dfs-slave | [Repo](https://github.com/juju-solutions/interface-dfs-slave.git) | [Docs](https://github.com/juju-solutions/interface-dfs-slave.git#readme) | dfs-slave | Interface layer for the DataNode <-> NameNode protocol |
| dfs | [Repo](https://github.com/juju-solutions/interface-dfs.git) | [Docs](https://github.com/juju-solutions/interface-dfs.git#readme) | dfs | Interface layer for the hdfs interface protocol |
| dm-node | [Repo](https://code.launchpad.net/~ibmcharmers/interface-ibm-dm-node/trunk) | [Docs](https://bazaar.launchpad.net/~ibmcharmers/interface-ibm-dm-node/files/README.md) | dm-node | This interface handles the comunication between IBM WAS ND DM and IBM WAS ND Node charms |
| docker-image-host | [Repo](https://github.com/tengu-team/interface-docker-image-host) | [Docs](https://github.com/tengu-team/interface-docker-image-host#readme) | docker-image-host | Interface to send image to docker host |
| docker-registry | [Repo](https://github.com/juju-solutions/interface-docker-registry.git) | [Docs](https://github.com/juju-solutions/interface-docker-registry.git#readme) | docker-registry | Interface layer for connecting to the Docker Registry charm |
| dockerhost | [Repo](https://github.com/juju-solutions/interface-dockerhost) | [Docs](https://github.com/juju-solutions/interface-dockerhost#readme) | dockerhost | Docker connection information for a unit |
| druid-config | [Repo](https://gitlab.com/spiculedata/juju/druid-config-relation.git) | [Docs](https://gitlab.com/spiculedata/juju/druid-config-relation.git) | Druid Configuration | Configuration layer for Spicule's Druid charms. |
| elastic-beats | [Repo](https://github.com/juju-solutions/interface-elastic-beats) | [Docs](https://github.com/juju-solutions/interface-elastic-beats#readme) | elastic-beats | Interface for elastic beats |
| elasticsearch | [Repo](http://github.com/juju-solutions/interface-elasticsearch) | [Docs](http://github.com/juju-solutions/interface-elasticsearch#readme) | elasticsearch | Interface to connect with elasticsearch. |
| etcd-proxy | [Repo](https://github.com/juju-solutions/interface-etcd-proxy) | [Docs](https://github.com/juju-solutions/interface-etcd-proxy#readme) | etcd-proxy | Do you need etcd as a read/readwrite proxy to a cluster? use this interface. |
| etcd | [Repo](https://github.com/juju-solutions/interface-etcd) | [Docs](https://github.com/juju-solutions/interface-etcd#readme) | etcd | Interface for relating to etcd |
| flume-agent | [Repo](https://github.com/juju-solutions/interface-flume-agent.git) | [Docs](https://github.com/juju-solutions/interface-flume-agent.git#readme) | flume-agent | Interface layer for communication between Apache Flume charms |
| gcp-integration | [Repo](https://github.com/juju-solutions/interface-gcp-integration.git) | [Docs](https://github.com/juju-solutions/interface-gcp-integration.git#readme) | gcp-integration | Interface layer for connecting to the GCP integration charm |
| generic-ip-port-user-pass | [Repo](https://git.launchpad.net/generic-ip-port-user-pass-charm-interface) | [Docs](https://git.launchpad.net/tree/README.md) | generic-ip-port-user-pass | An interface for reactive charms needing to pass generic IP (or URL), port, username and password data |
| giraph | [Repo](https://github.com/juju-solutions/interface-giraph) | [Docs](https://github.com/juju-solutions/interface-giraph#readme) | giraph | This interface handles the communication between Apache Giraph and its clients |
| gluster-fuse | [Repo](https://github.com/cholcombe973/juju-interface-gluster-fuse) | [Docs](https://github.com/cholcombe973/juju-interface-gluster-fuse#readme) | gluster-fuse | Distributed posix storage provided by GlusterFS |
| gluster-nfs | [Repo](https://github.com/cholcombe973/juju-interface-gluster-client) | [Docs](https://github.com/cholcombe973/juju-interface-gluster-client#readme) | gluster-nfs | Scale out NFS provided by GlusterFS |
| gluster-peer | [Repo](https://github.com/wolsen/charm-interface-gluster-peer) | [Docs](https://github.com/wolsen/charm-interface-gluster-peer#readme) | gluster-peer | Peer interface for glusterfs nodes |
| gnocchi | [Repo](https://github.com/openstack/charm-interface-gnocchi) | [Docs](https://github.com/openstack/charm-interface-gnocchi#readme) | gnocchi | Gnocchi Metrics Service interface |
| gpfs | [Repo](https://code.launchpad.net/~ibmcharmers/interface-ibm-gpfs/trunk) | [Docs](https://bazaar.launchpad.net/~ibmcharmers/interface-ibm-gpfs/files/README.md) | gpfs | Interface layer between IBM Spectrum Scale Manager and IBM Spectrum Scale client as well as peer communication among manager/client units |
| grafana-dashboard | [Repo](https://github.com/juju-solutions/interface-grafana-dashboard) | [Docs](https://github.com/juju-solutions/interface-grafana-dashboard#readme) | grafana-dashboard | Interface layer for importing dashboards into Grafana |
| grafana-source | [Repo](https://git.launchpad.net/interface-grafana-source) | [Docs](https://git.launchpad.net/tree/README.md) | grafana-source | Grafana source |
| hacluster | [Repo](https://github.com/openstack/charm-interface-hacluster.git) | [Docs](https://github.com/openstack/charm-interface-hacluster.git#readme) | hacluster | hacluster interface for relations with hacluster subordinate charm |
| hadoop-plugin | [Repo](https://github.com/juju-solutions/interface-hadoop-plugin.git) | [Docs](https://github.com/juju-solutions/interface-hadoop-plugin.git#readme) | hadoop-plugin | Interface for relating to Apache Hadoop |
| hadoop-rest | [Repo](https://github.com/juju-solutions/interface-hadoop-rest) | [Docs](https://github.com/juju-solutions/interface-hadoop-rest#readme) | hadoop-rest | Interface layer for connecting to hadoop-plugin without installation |
| hbase-quorum | [Repo](https://github.com/juju-solutions/interface-hbase-quorum.git) | [Docs](https://github.com/juju-solutions/interface-hbase-quorum.git#readme) | hbase quorum | This interface layer handles the communication among Apache HBase peers |
| hbase | [Repo](https://github.com/juju-solutions/interface-hbase.git) | [Docs](https://github.com/juju-solutions/interface-hbase.git#readme) | hbase | This interface layer handles the communication between Apache HBase and its clients |
| hive | [Repo](https://github.com/juju-solutions/interface-hive.git) | [Docs](https://github.com/juju-solutions/interface-hive.git#readme) | hive | Interface for relating to Apache Hive |
| http | [Repo](https://github.com/juju-solutions/interface-http.git) | [Docs](https://github.com/juju-solutions/interface-http.git#readme) | http | HTTP Relation Stub |
| https | [Repo](https://code.launchpad.net/~ibmcharmers/interface-https/trunk) | [Docs](https://bazaar.launchpad.net/~ibmcharmers/interface-https/files/README.md) | https |  Basic HTTPS interface |
| ibm-db2 | [Repo](https://launchpad.net/~ibmcharmers/interface-ibm-db2/trunk) | [Docs](https://bazaar.launchpad.net/~ibmcharmers/interface-ibm-db2/files/README.md) | ibm-db2 | This interface layer handles the communication between  IBM DB2 and Consumer charms. |
| ibm-mq | [Repo](https://code.launchpad.net/~ibmcharmers/interface-ibm-mq/trunk) | [Docs](https://bazaar.launchpad.net/~ibmcharmers/interface-ibm-mq/files/README.md) | ibm-mq | This interface handles the communication between IBM MQ and other consumer charms. |
| ibm-wxs | [Repo](https://launchpad.net/~ibmcharmers/interface-ibm-wxs/trunk) | [Docs](https://bazaar.launchpad.net/~ibmcharmers/interface-ibm-wxs/files/README.md) | ibm-wxs | This interface layer handles the communication between  IBM WXS Catalog charm and other consumer charms, such as IBM WXS Container and IBM WXS Client |
| ignite-hadoop | [Repo](https://github.com/juju-solutions/interface-ignite-hadoop) | [Docs](https://github.com/juju-solutions/interface-ignite-hadoop#readme) | ignite-hadoop | Minimal interface layer for connecting Apache Ignite-Hadoop to Apache Hadoop slave |
| influxdb-api | [Repo](https://github.com/ChrisMacNaughton/interface-influxdb-api.git) | [Docs](https://github.com/ChrisMacNaughton/interface-influxdb-api.git#readme) | influxdb-api | InfluxDB Query Interface |
| infoblox | [Repo](https://github.com/openstack-charmers/interface-infoblox.git) | [Docs](https://github.com/openstack-charmers/interface-infoblox.git#readme) | infoblox | Interface layer between infoblox and neutron-api |
| ironic-api | [Repo](https://opendev.org/openstack/charm-interface-ironic-api.git) | [Docs](https://opendev.org/openstack/charm-interface-ironic-api/src/branch/master/README.md) | ironic-api | Ironic API provides and requires interfaces |
| java | [Repo](https://github.com/juju-solutions/interface-java.git) | [Docs](https://github.com/juju-solutions/interface-java.git#readme) | java | Interface for relating to subordinate charms providing a Java runtime or JDK |
| jdbc | [Repo](https://gitlab.com/spiculedata/juju/jdbc-interface.git) | [Docs](https://gitlab.com/spiculedata/juju/jdbc-interface.git) | jdbc | JDBC interface for generic connectivity across databases |
| jenkins-extension | [Repo](https://github.com/juju-solutions/interface-jenkins-extension.git) | [Docs](https://github.com/juju-solutions/interface-jenkins-extension.git#readme) | jenkins-extension | Admin interface to the jenkins master |
| jenkins-slave | [Repo](https://github.com/freeekanayaka/interface-jenkins-slave.git) | [Docs](https://github.com/freeekanayaka/interface-jenkins-slave.git#readme) | jenkins-slave | Communication between a Jenkins master and a Jenkins slave |
| jenkins-zuul | [Repo](https://github.com/freeekanayaka/interface-jenkins-zuul.git) | [Docs](https://github.com/freeekanayaka/interface-jenkins-zuul.git#readme) | jenkins-zuul | communication between a Jenkins master and Zuul Jenkins via the zuul interface |
| juju-info | [Repo](https://github.com/juju-solutions/interface-juju-info.git) | [Docs](https://github.com/juju-solutions/interface-juju-info.git#readme) | juju-info | Implied interface for subordinates with special behavior. This is not a substitute for a proper relationship interface.  |
| kafka | [Repo](https://github.com/juju-solutions/interface-kafka.git) | [Docs](https://github.com/juju-solutions/interface-kafka.git#readme) | kafka | Interface layer for communication between Kafka and its clients |
| kapacitor | [Repo](https://github.com/tengu-team/interface-kapacitor.git) | [Docs](https://github.com/tengu-team/interface-kapacitor.git#readme) | kapacitor | Interface layer for Kapacitor |
| keystone-admin | [Repo](https://github.com/openstack/charm-interface-keystone-admin) | [Docs](https://github.com/openstack/charm-interface-keystone-admin#readme) | keystone-admin | keystone-admin:identity-admin interface to use shared admin API credentials |
| keystone-credentials | [Repo](https://github.com/openstack/charm-interface-keystone-credentials) | [Docs](https://github.com/openstack/charm-interface-keystone-credentials#readme) | keystone-credentials | keystone-credentials: Interface for integrating with Keystone identity credentials |
| keystone-domain-backend | [Repo](https://github.com/openstack/charm-interface-keystone-domain-backend) | [Docs](https://github.com/openstack/charm-interface-keystone-domain-backend#readme) | keystone-domain-backend | Interface for integration of subordinate charms providing domain specific identity backends |
| keystone-fid-service-provider | [Repo](https://github.com/openstack/charm-interface-keystone-fid-service-provider) | [Docs](https://github.com/openstack/charm-interface-keystone-fid-service-provider#readme) | keystone-fid-service-provider | An interface to connect a federated identity provider to the Keystone charm |
| keystone-notifications | [Repo](https://github.com/openstack/charm-interface-keystone-notifications) | [Docs](https://github.com/openstack/charm-interface-keystone-notifications#readme) | keystone-notifications | keystone-notifications: Interface for integrating with Keystone notifications |
| keystone | [Repo](https://github.com/openstack/charm-interface-keystone) | [Docs](https://github.com/openstack/charm-interface-keystone#readme) | keystone | Keystone interface |
| kube-control | [Repo](https://github.com/juju-solutions/interface-kube-control.git) | [Docs](https://github.com/juju-solutions/interface-kube-control.git#readme) | kube-control | master-worker control interface for Kubernetes |
| kube-dns | [Repo](https://github.com/juju-solutions/interface-kube-dns.git) | [Docs](https://github.com/juju-solutions/interface-kube-dns.git#readme) | kube-dns | Kubernetes DNS Details |
| kube-masters | [Repo](https://github.com/charmed-kubernetes/interface-kube-masters.git) | [Docs](https://github.com/charmed-kubernetes/interface-kube-masters.git#readme) | Kubernetes Master Peers | Interface for kubernetes-master peers |
| kubernetes-cni | [Repo](https://github.com/juju-solutions/interface-kubernetes-cni) | [Docs](https://github.com/juju-solutions/interface-kubernetes-cni#readme) | kubernetes-cni | Interface for relating various CNI implementations |
| limeds | [Repo](https://github.com/tengu-team/interface-limeds) | [Docs](https://github.com/tengu-team/interface-limeds#readme) | limeds | Interface to connect to LimeDS |
| livy | [Repo](https://gitlab.com/spiculedata/juju/livy-relation.git) | [Docs](https://gitlab.com/spiculedata/juju/livy-relation.git) | Apache Livy relation | Relation to connect a charm to Apache Livy. |
| local-monitors | [Repo](https://github.com/cmars/local-monitors-interface) | [Docs](https://github.com/cmars/local-monitors-interface#readme) | local-monitors | relation for registering nagios checks |
| logstash-client | [Repo](https://github.com/juju-solutions/interface-logstash-client) | [Docs](https://github.com/juju-solutions/interface-logstash-client#readme) | logstash-client | Interface for connecting with logstash based systems. |
| magpie | [Repo](https://opendev.org/openstack/charm-interface-magpie.git) | [Docs](https://opendev.org/openstack/charm-interface-magpie.git) | magpie | This interface layer handles the communication among Magpie peers. |
| mahout | [Repo](https://github.com/juju-solutions/interface-mahout) | [Docs](https://github.com/juju-solutions/interface-mahout#readme) | mahout | This interface layer handles the communication between Apache Mahout and its clients |
| manila-plugin | [Repo](https://github.com/openstack/charm-interface-manila-plugin) | [Docs](https://github.com/openstack/charm-interface-manila-plugin#readme) | manila-plugin | manila-plugin: configuration plugin to allow manila plugins to configure the manila service |
| mapred-slave | [Repo](https://github.com/juju-solutions/interface-mapred-slave.git) | [Docs](https://github.com/juju-solutions/interface-mapred-slave.git#readme) | mapred-slave | Interface layer for the NodeManager <-> ResourceManager protocol |
| mapred | [Repo](https://github.com/juju-solutions/interface-mapred.git) | [Docs](https://github.com/juju-solutions/interface-mapred.git#readme) | mapred | Interface for the YARN client protocol |
| memcache | [Repo](https://github.com/omnivector-solutions/interface-memcache.git) | [Docs](https://github.com/omnivector-solutions/interface-memcache.git#readme) | Memcache | Interface for relating memcache. |
| midonet-api | [Repo](https://github.com/celebdor/interface-midonet-api.git) | [Docs](https://github.com/celebdor/interface-midonet-api.git#readme) | MidoNet API | MidoNet API interface between provider and consuming charms |
| mongodb-cluster | [Repo](https://github.com/tkuhlman/juju-relation-mongodb) | [Docs](https://github.com/tkuhlman/juju-relation-mongodb#readme) | mongodb-cluster | relation to connect to a mongo database cluster |
| mongodb | [Repo](https://github.com/cloud-green/juju-relation-mongodb) | [Docs](https://github.com/cloud-green/juju-relation-mongodb#readme) | mongodb | relation to connect to a mongo database |
| monitor | [Repo](https://github.com/juju-solutions/interface-monitor.git) | [Docs](https://github.com/juju-solutions/interface-monitor.git#readme) | monitor | This interface layer for monitor protocol |
| mount | [Repo](https://github.com/juju-solutions/interface-mount.git) | [Docs](https://github.com/juju-solutions/interface-mount.git#readme) | mount | Interface layer for connecting mounts to a charm such as NFS |
| munge-auth | [Repo](https://github.com/omnivector-solutions/interface-munge-auth) | [Docs](https://github.com/omnivector-solutions/interface-munge-auth#readme) | munge-auth | Interface layer for Munge Auth |
| munin-node | [Repo](https://github.com/freyes/interface-munin-node) | [Docs](https://github.com/freyes/interface-munin-node#readme) | munin-node | munin-node relation |
| munin | [Repo](https://github.com/freyes/interface-munin) | [Docs](https://github.com/freyes/interface-munin#readme) | munin | munin relation |
| mysql-admin | [Repo](https://github.com/charmed-osm/mysql-interface) | [Docs](https://github.com/charmed-osm/mysql-interface#readme) | mysql-admin | MySQL interface with root and non-root admin access to connected applications |
| mysql-innodb-cluster | [Repo](https://github.com/openstack/charm-interface-mysql-innodb-cluster.git) | [Docs](https://github.com/openstack/charm-interface-mysql-innodb-cluster/blob/master/README.md) | mysql-innodb-cluster | MySQL InnoDB Cluster peer interface |
| mysql-root | [Repo](https://github.com/juju-solutions/interface-mysql-root.git) | [Docs](https://github.com/juju-solutions/interface-mysql-root.git#readme) | mysql-root | Administrative MySQL interface with admin access granted to connected applications |
| mysql-router | [Repo](https://github.com/openstack/charm-interface-mysql-router.git) | [Docs](https://github.com/openstack/charm-interface-mysql-router/blob/master/README.md) | mysql-router | MySQL Router provides and requiers interfaces |
| mysql-shared | [Repo](https://github.com/openstack/charm-interface-mysql-shared) | [Docs](https://github.com/openstack/charm-interface-mysql-shared#readme) | mysql-shared | MySQL Shared Database interface |
| mysql | [Repo](https://github.com/johnsca/juju-relation-mysql.git) | [Docs](https://github.com/johnsca/juju-relation-mysql.git#readme) | mysql | Standard MySQL interface with generated, per-service databases |
| namenode-cluster | [Repo](https://github.com/juju-solutions/interface-namenode-cluster.git) | [Docs](https://github.com/juju-solutions/interface-namenode-cluster.git#readme) | namenode-cluster | Interface layer for running Apache Hadoop NameNode as HA |
| neutron-load-balancer | [Repo](https://github.com/openstack/charm-interface-neutron-load-balancer.git) | [Docs](https://github.com/openstack/charm-interface-neutron-load-balancer.git#readme) | neutron-load-balancer | Interface supporting the integration between Neutron and external Load Balancer services |
| neutron-plugin-api-subordinate | [Repo](https://github.com/openstack/charm-interface-neutron-plugin-api-subordinate) | [Docs](https://github.com/openstack/charm-interface-neutron-plugin-api-subordinate#readme) | neutron-plugin-api-subordinate | This interface is used for a charm to send configuration information to the neutron-api principle charm and request a restart of a service managed by that charm. |
| neutron-plugin-zlmao | [Repo](https://github.com/openstack/charm-interface-neutron-plugin) | [Docs](https://github.com/openstack/charm-interface-neutron-plugin#readme) | neutron-plugin | Interface for intergrating Neutron SDN with the nova-compute charm |
| neutron-plugin | [Repo](https://github.com/openstack/charm-interface-neutron-plugin) | [Docs](https://github.com/openstack/charm-interface-neutron-plugin#readme) | neutron-plugin | Interface for intergrating Neutron SDN with the nova-compute charm |
| nfsstorage | [Repo](https://launchpad.net/~ibmcharmers/interface-ibm-nfsstorage/trunk) | [Docs](https://bazaar.launchpad.net/~ibmcharmers/interface-ibm-nfsstorage/files/README.md) | nfsstorage | This interface layer handles the communication between LSF/Spectrum Symphony Storage which is acting as a NFS Server and NFS Clients like Platform LSF Master, Spectrum Symphony Master. |
| nginx-stats | [Repo](https://github.com/silph-io/interface-nginx-stats) | [Docs](https://github.com/silph-io/interface-nginx-stats#readme) | NGINX Stats | NGINX stats/status protocol |
| nova-cell | [Repo](https://github.com/openstack/charm-interface-nova-cell.git) | [Docs](https://github.com/openstack/charm-interface-nova-cell.git#readme) | nova-cell | Interface supporting the integration between Nova super conductor and nova cell |
| nova-compute | [Repo](https://github.com/openstack/charm-interface-nova-compute.git) | [Docs](https://github.com/openstack/charm-interface-nova-compute.git#readme) | nova-compute | Interface supporting the integration between Nova controller and compute nodes |
| nrpe-external-master | [Repo](https://github.com/cmars/nrpe-external-master-interface) | [Docs](https://github.com/cmars/nrpe-external-master-interface#readme) | nrpe-external-master | relation for registering nagios checks |
| nrpe | [Repo](https://github.com/alejdg/nrpe-interface) | [Docs](https://github.com/alejdg/nrpe-interface#readme) | nrpe | relation for registering nagios checks |
| odl-controller-api | [Repo](https://github.com/openstack/charm-interface-odl-controller-api) | [Docs](https://github.com/openstack/charm-interface-odl-controller-api#readme) | odl-controller-api | Interface for intergrating with an OpenDayLight Controller RESTful API |
| oidc-client | [Repo](https://github.com/juju-solutions/interface-oidc-client.git) | [Docs](https://github.com/juju-solutions/interface-oidc-client.git#readme) | oidc-client | Interface layer for the OIDC Clients |
| oozie | [Repo](https://gitlab.com/spiculedata/juju/oozie-interface.git) | [Docs](https://gitlab.com/spiculedata/juju/oozie-interface.git) | oozie | Connection for oozie to consumers |
| openstack-ha | [Repo](https://github.com/openstack/charm-interface-openstack-ha) | [Docs](https://github.com/openstack/charm-interface-openstack-ha#readme) | openstack-ha | Interface for managing information with peers in the same OpenStack service |
| openstack-integration | [Repo](https://github.com/juju-solutions/interface-openstack-integration.git) | [Docs](https://github.com/juju-solutions/interface-openstack-integration.git#readme) | openstack-integration | Interface layer for connecting to the OpenStack integrator charm |
| opentsdb | [Repo](https://github.com/tengu-team/interface-opentsdb.git) | [Docs](https://github.com/tengu-team/interface-opentsdb.git#readme) | opentsdb | Interface layer for OpenTSDB. |
| ovsdb-cluster | [Repo](https://opendev.org/x/charm-interface-ovsdb.git) | [Docs](https://opendev.org/x/charm-interface-ovsdb/src/branch/master/src/ovsdb_cluster/README.md) | ovsdb-cluster | Interface for OVN OVSDB Cluster |
| ovsdb-cms | [Repo](https://opendev.org/x/charm-interface-ovsdb.git) | [Docs](https://opendev.org/x/charm-interface-ovsdb/src/branch/master/src/ovsdb_cms/README.md) | ovsdb-cms | Interface for a OVN CMS to talk to a OVSDB Cluster |
| ovsdb-manager | [Repo](https://github.com/openstack/charm-interface-ovsdb-manager) | [Docs](https://github.com/openstack/charm-interface-ovsdb-manager#readme) | ovsdb-manager | Interface for relating to the OVSDB manager aspect of OpenDayLight SDN |
| ovsdb-subordinate | [Repo](https://opendev.org/x/charm-interface-ovsdb.git) | [Docs](https://opendev.org/x/charm-interface-ovsdb/src/branch/master/src/ovsdb_subordinate/README.md) | ovsdb-subordinate | Interface for subordinate relation between ovn-chassis and principle |
| ovsdb | [Repo](https://opendev.org/x/charm-interface-ovsdb.git) | [Docs](https://opendev.org/x/charm-interface-ovsdb/src/branch/master/src/ovsdb/README.md) | ovsdb | Interface for OVN consumers to talk to a OVSDB Cluster |
| pacemaker-remote | [Repo](https://github.com/openstack/charm-interface-pacemaker-remote.git) | [Docs](https://github.com/openstack/charm-interface-pacemaker-remote.git#readme) | pacemaker-remote | Interface for registering a pacemaker remote node with a cluster. |
| panko | [Repo](https://github.com/openstack-charmers/charm-interface-panko) | [Docs](https://github.com/openstack-charmers/charm-interface-panko#readme) | panko | Panko Event Service interface |
| peer-discovery | [Repo](https://github.com/tbaumann/charm-interface-peer-discovery) | [Docs](https://github.com/tbaumann/charm-interface-peer-discovery#readme) | peer-discovery | [proposal] simple interface to discover all peers of a charm through peer relation |
| pgsql | [Repo](https://git.launchpad.net/interface-pgsql) | [Docs](https://interface-pgsql.readthedocs.io/en/stable/) | pgsql | Postgresql database client interface |
| placement | [Repo](https://opendev.org/openstack/charm-interface-placement) | [Docs](https://opendev.org/openstack/charm-interface-placement) | placement | Interface for migrating placement API from nova-cloud-controller to placement charm. |
| platformmaster | [Repo](https://launchpad.net/~ibmcharmers/interface-ibm-platformmaster/trunk) | [Docs](https://bazaar.launchpad.net/~ibmcharmers/interface-ibm-platformmaster/files/README.md) | platformmaster | This interface layer handles the communication between Platform Master (like IBM Platform LSF, IBM Spectrum Symphony) and Platform Server/Nodes. |
| prometheus-manual | [Repo](https://github.com/juju-solutions/interface-prometheus-manual) | [Docs](https://github.com/juju-solutions/interface-prometheus-manual#readme) | prometheus-manual | Interface layer for register manual scrape job configuration stanzas with Prometheus 2 |
| prometheus-rules | [Repo](https://github.com/CanonicalBootStack/interface-prometheus-rules.git) | [Docs](https://github.com/CanonicalBootStack/interface-prometheus-rules.git#readme) | prometheus-rules | Relation Stub to export Prometheus alerting rules |
| prometheus | [Repo](https://git.launchpad.net/interface-prometheus) | [Docs](https://git.launchpad.net/tree/README.md) | prometheus | Prometheus target interface |
| public-address | [Repo](https://github.com/juju-solutions/interface-public-address) | [Docs](https://github.com/juju-solutions/interface-public-address#readme) | public-address | Simple relation that provides the providers public-address and a port |
| rabbitmq | [Repo](https://github.com/openstack/charm-interface-rabbitmq) | [Docs](https://github.com/openstack/charm-interface-rabbitmq#readme) | rabbitmq | RabbitMQ AMQP interface |
| redis | [Repo](https://github.com/omnivector-solutions/interface-redis) | [Docs](https://github.com/omnivector-solutions/interface-redis#readme) | redis | Interface for relating to redis |
| rsyslog | [Repo](https://bazaar.launchpad.net/~canonical-sysadmins/canonical-is-charms/layer-rsyslog/files) | [Docs](https://bazaar.launchpad.net/~canonical-sysadmins/canonical-is-charms/layer-rsyslog/files/README.md) | Rsyslog layer | This rsyslog layer will enable rsyslog and enable building additional logging configuration. |
| sdn-plugin | [Repo](https://github.com/juju-solutions/interface-sdn-plugin) | [Docs](https://github.com/juju-solutions/interface-sdn-plugin#readme) | sdn-plugin | An abstraction of common configurations for SDN providers, to be consumed by charms |
| service-control | [Repo](https://github.com/openstack/charm-interface-service-control) | [Docs](https://github.com/openstack/charm-interface-service-control#readme) | service-control | This interface is used for a charm to request a restart of a service managed by another charm. |
| service-mesh | [Repo](https://github.com/juju-solutions/interface-service-mesh.git) | [Docs](https://github.com/juju-solutions/interface-service-mesh.git#readme) | service-mesh | Generic Service Mesh interface layer |
| slurm-cluster | [Repo](https://github.com/omnivector-solutions/interface-slurm-cluster) | [Docs](https://github.com/omnivector-solutions/interface-slurm-cluster#readme) | slurm-cluster | Interface layer for Slurm |
| slurm-controller-ha | [Repo](https://github.com/omnivector-solutions/interface-slurm-controller-ha) | [Docs](https://github.com/omnivector-solutions/interface-slurm-controller-ha#readme) | slurm-controller-ha | Interface layer for Slurm-Controller-HA |
| slurm-dbd-ha | [Repo](https://github.com/omnivector-solutions/interface-slurm-dbd-ha) | [Docs](https://github.com/omnivector-solutions/interface-slurm-dbd-ha#readme) | slurm-dbd-ha | Interface layer for Slurm-DBD-HA |
| slurm-dbd | [Repo](https://github.com/omnivector-solutions/interface-slurm-dbd) | [Docs](https://github.com/omnivector-solutions/interface-slurm-dbd#readme) | slurm-dbd | Interface layer for Slurm-DBD |
| solr | [Repo](https://github.com/buggtb/interface-solr) | [Docs](https://github.com/buggtb/interface-solr#readme) | solr | Solr Charm Interface |
| spark-quorum | [Repo](https://github.com/juju-solutions/interface-spark-quorum.git) | [Docs](https://github.com/juju-solutions/interface-spark-quorum.git#readme) | spark quorum | This interface layer handles the communication among Apache Spark peers |
| spark | [Repo](https://github.com/juju-solutions/interface-spark.git) | [Docs](https://github.com/juju-solutions/interface-spark.git#readme) | spark | Interface layer for the spark interface protocol |
| spectrum-scale-client | [Repo](https://code.launchpad.net/~ibmcharmers/interface-spectrum-scale-client/trunk) | [Docs](https://bazaar.launchpad.net/~ibmcharmers/interface-spectrum-scale-client/files/README.md) | spectrum-scale-client | Basic interface required for communication between Spectrum Scale client and IBM Cinder SpectrumScale (driver for gpfs) |
| syslog | [Repo](https://github.com/juju-solutions/interface-syslog.git) | [Docs](https://github.com/juju-solutions/interface-syslog.git#readme) | syslog | Interface layer for the syslog protocol |
| tls-certificates | [Repo](https://github.com/juju-solutions/interface-tls-certificates) | [Docs](https://github.com/juju-solutions/interface-tls-certificates#readme) | tls-certificates | An interface for exchanging tls certificates using provides and requres relations. |
| tls | [Repo](https://github.com/juju-solutions/interface-tls) | [Docs](https://github.com/juju-solutions/interface-tls#readme) | tls | The TLS interface provides a peering relationship to exchange certificates and CSR's. |
| untrusted-container-runtime | [Repo](https://github.com/charmed-kubernetes/interface-untrusted-container-runtime) | [Docs](https://github.com/charmed-kubernetes/interface-untrusted-container-runtime#readme) | Untrusted Container Runtime | Interface for a runtime to handle untrusted workloads. |
| vault-kv | [Repo](https://github.com/openstack-charmers/charm-interface-vault-kv.git) | [Docs](https://github.com/openstack-charmers/charm-interface-vault-kv.git#readme) | vault-kv | Interface layer for the vault-kv protocol |
| vault | [Repo](https://github.com/ChrisMacNaughton/juju-interface-vault.git) | [Docs](https://github.com/ChrisMacNaughton/juju-interface-vault.git#readme) | vault | Hashicorp Vault omterface |
| vsphere-integration | [Repo](https://github.com/juju-solutions/interface-vsphere-integration.git) | [Docs](https://github.com/juju-solutions/interface-vsphere-integration.git#readme) | vsphere-integration | Interface layer for connecting to the VMware vSphere integration charm |
| was-ihs | [Repo](https://code.launchpad.net/~ibmcharmers/interface-ibm-was-ihs/trunk) | [Docs](https://bazaar.launchpad.net/~ibmcharmers/interface-ibm-was-ihs/files/README.md) | was-ihs | This Interface handles the communication between IBM WAS Base/IBM WAS ND and IBM Http Server |
| was-nd | [Repo](https://code.launchpad.net/~ibmcharmers/interface-ibm-was-nd/trunk) | [Docs](https://bazaar.launchpad.net/~ibmcharmers/interface-ibm-was-nd/files/README.md) | was-nd | This interface handles the communication between IBM WAS ND DM and other consumer charms. |
| websso-fid-service-provider | [Repo](https://github.com/openstack/charm-interface-websso-fid-service-provider) | [Docs](https://github.com/openstack/charm-interface-websso-fid-service-provider#readme) | websso-fid-service-provider | An interface to connect a federated identity provider to OpenStack dashboard charm |
| weebl | [Repo](https://github.com/autonomouse/interface-weebl) | [Docs](https://github.com/autonomouse/interface-weebl#readme) | weebl | Interface for relating to the OIL dashboard (Weebl) |
| wsgi | [Repo](https://git.launchpad.net/~ubuntuone-hackers/charms/+source/interface-wsgi) | [Docs](https://git.launchpad.net/~ubuntuone-hackers/charms/+source/tree/README.md) | wsgi | Basic WSGI interface |
| zeppelin | [Repo](https://github.com/juju-solutions/interface-zeppelin) | [Docs](https://github.com/juju-solutions/interface-zeppelin#readme) | zeppelin | Interface layer for interacting with charms for Apache Zeppelin |
| zookeeper-quorum | [Repo](https://github.com/juju-solutions/interface-zookeeper-quorum.git) | [Docs](https://github.com/juju-solutions/interface-zookeeper-quorum.git#readme) | zookeeper quorum | This interface layer handles the communication among Apache Zookeeper peers |
| zookeeper | [Repo](https://github.com/juju-solutions/interface-zookeeper.git) | [Docs](https://github.com/juju-solutions/interface-zookeeper.git#readme) | zookeeper | This interface layer handles the communication between Apache Zookeeper and its clients |

<!-- /list-of-interfaces -->
