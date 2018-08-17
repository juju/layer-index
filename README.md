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

| ID | Name | Summary |
| --- | --- | --- |
| [ansible-base](https://github.com/chuckbutler/ansible-base) | ansible-base | Base / charm layer for charming w/ Ansible |
| [apache-bigtop-base](https://github.com/juju-solutions/layer-apache-bigtop-base.git) | Apache Bigtop Base Layer | Base layer for charms needing Apache Bigtop  |
| [apache-bigtop-gateway](https://github.com/juju-solutions/layer-apache-bigtop-gateway) | apache-bigtop-gateway | Base layer for Gateway node from Apache Big Top |
| [apache-flume-base](https://github.com/juju-solutions/layer-apache-flume-base.git) | Apache Flume Base | Base layer for Apache Flume charms |
| [apache-hadoop-datanode](https://github.com/juju-solutions/layer-apache-hadoop-datanode.git) | Apache Hadoop DataNode | Base / charm layer for the DataNode component of Hadoop |
| [apache-hadoop-namenode](https://github.com/juju-solutions/layer-apache-hadoop-namenode.git) | Apache Hadoop NameNode | Charm layer for the NameNode component of Hadoop |
| [apache-hadoop-nodemanager](https://github.com/juju-solutions/layer-apache-hadoop-nodemanager.git) | Apache Hadoop NodeManager | Base / charm layer for the NodeManager component of Hadoop |
| [apache-hadoop-plugin](https://github.com/juju-solutions/layer-apache-hadoop-plugin.git) | apache-hadoop-plugin | Simplified connection point for Apache Hadoop platform |
| [apache-hadoop-resourcemanager](https://github.com/juju-solutions/layer-apache-hadoop-resourcemanager.git) | Apache Hadoop ResourceManager | Charm layer for the ResourceManager component of Hadoop |
| [apache-hadoop-slave](https://github.com/juju-solutions/layer-apache-hadoop-slave.git) | apache-hadoop-slave | Combined slave node (DataNode + NodeManager) for Apache Hadoop |
| [apache-php](https://github.com/juju-solutions/layer-apache-php.git) | Apache PHP base layer | Configurable base for Apache PHP charms |
| [apache-wsgi](https://git.launchpad.net/~jacekn/charms/+source/apache-wsgi) | Apache WSGI base layer | Configurable base for Apache WSGI charms |
| [apt](https://git.launchpad.net/layer-apt) | Apt layer | Easily deal with apt sources and deb packages |
| [barbican-client](https://github.com/omnivector-solutions/layer-barbican-client) | Barbican Client | Reactive layer to help pull secrets from barbican |
| [basic](https://github.com/juju-solutions/layer-basic.git) | Basic Layer | Base layer for charms with the Reactive framework |
| [beats-base](https://github.com/juju-solutions/layer-beats-base) | Beats Base | Base layer for Elastic Beats |
| [bigtop-base](https://github.com/juju-solutions/layer-apache-bigtop-base.git) | Apache Bigtop Base Layer | Base layer for charms needing Apache Bigtop  |
| [buildpacks](https://git.launchpad.net/~bcsaller/charms/+source/buildpacks) | Buildpacks | Experimental layer for using buildpacks to generate Charmed applications |
| [caas-base](https://github.com/juju-solutions/layer-caas-base.git) | Base Layer for CAAS charms | Base layer for CAAS charms with the Reactive framework |
| [cdk-service-kicker](https://github.com/juju-solutions/layer-cdk-service-kicker.git) | CDK Service Kicker | Installs a background service, cdk-service-kicker, for kicking cdk services. |
| [ceph-base](https://github.com/ChrisMacNaughton/layer-ceph-base) | EXPERIMENTAL Ceph Base Layer | EXPERIMENTAL Ceph base layer |
| [ceph-basic](https://github.com/ChrisMacNaughton/layer-ceph-basic) | EXPERIMENTAL ceph-basic | EXPERIMENTAL ceph-basic layer |
| [ceph-mon](https://github.com/ChrisMacNaughton/juju-layer-ceph-mon) | EXPERIMENTAL Ceph Mon layer | EXPERIMENTAL Ceph Mon layer |
| [charmscaler-base](https://github.com/elastisys/layer-charmscaler-base) | Charmscaler Base | Charmscaler base layer |
| [conda-api](https://github.com/omnivector-solutions/layer-conda-api) | Conda API | Conda API layer |
| [consul-base](https://github.com/omnivector-solutions/layer-consul-base) | Consul Base | Reactive base layer for consul |
| [coordinator](https://git.launchpad.net/layer-coordinator ) | Coordinator Layer | Coordinate operations between units in a service, such as rolling restarts. |
| [debug](https://github.com/juju-solutions/layer-debug.git) | debug | Provides a troubleshooting debug action |
| [django](https://github.com/marcoceppi/layer-django.git) | Django | Django / GUNICORN |
| [docker-resource](https://github.com/juju-solutions/layer-docker-resource.git) | Docker Resource Layer | Layer for managing charm resources of type 'docker' |
| [docker](https://github.com/juju-solutions/layer-docker.git) | Docker | Layer to deliver and install Docker on Ubuntu, Debian, Centos hosts. |
| [elastic-base](https://github.com/omnivector-solutions/layer-elastic-base.git) | Elastic-Base | Base layer for Elastic.co charms |
| [elasticsearch-client](https://github.com/omnivector-solutions/layer-elasticsearch-client) | Elasticsearch Client | Elasticsearch client layer |
| [elixir](https://github.com/battlemidget/juju-layer-elixir.git) | Elixir | Runtime layer for Elixir applications |
| [flannel](https://github.com/juju-solutions/layer-flannel) | Flannel | Flannel Overlay Network layer for docker |
| [flask](https://github.com/IBCNServices/layer-flask) | Flask | Layer to create Flask webservers running on nginx |
| [git-deploy](https://github.com/omnivector-solutions/layer-git-deploy.git) | Git Deploy | Layer to aid with deploying code from github |
| [go-binary](https://github.com/cloud-green/go-binary-layer) | Go Binary Base Layer | Takes a statically compiled go binary and starts it as a service |
| [hadoop-base](https://github.com/juju-solutions/layer-hadoop-base.git) | Hadoop Base | Base layer for a charm needing the Apache Hadoop libraries |
| [hadoop-client](https://github.com/juju-solutions/layer-hadoop-client.git) | hadoop-client | Base and charm layer for Hadoop clients |
| [hadoop-datanode](https://github.com/juju-solutions/layer-hadoop-datanode) | hadoop-datanode | Base layer for DataNode from Apache BigTop |
| [hadoop-ganglia](https://github.com/juju-solutions/layer-hadoop-ganglia.git) | hadoop-ganglia | Base layer for adding Ganglia support to Hadoop core charms |
| [hadoop-nodemanager](https://github.com/juju-solutions/layer-hadoop-nodemanager) | hadoop-nodemanager | Base layer for NodeManager from Apache BigTop |
| [haproxy-core](https://github.com/juju-solutions/layer-haproxy-core.git) | haproxy-core | A reactive layer that delivers a minimal haproxy layer to use in other application layers. |
| [hhvm](https://github.com/battlemidget/juju-layer-hhvm) | HHVM | Provides HHVM and composer for php applications |
| [ibm-base](https://code.launchpad.net/~ibmcharmers/layer-ibm-base/trunk) | IBM Base Layer | Base layer for IBM charms |
| [ibm-im](http://launchpad.net/~ibmcharmers/ibmlayers/layer-ibm-im) | IBM IM | This layer provides IBM Installation Manager, which can be used to install many IBM products. |
| [ibm-was-nd](https://code.launchpad.net/~ibmcharmers/charms/trusty/layer-ibm-was-nd/trunk) | IBM WAS ND | Charm layer for IBM WAS ND DM and WAS ND Node charms |
| [jenkins-workspace](https://github.com/juju-solutions/layer-jenkins-workspace) | Jenkins Workspace | Configure Jenkins with workspace snapshots |
| [jenkins](https://github.com/jenkinsci/jenkins-charm.git) | jenkins | Juju charm to deploy and scale Jenkins  |
| [juju-client](https://github.com/tengu-team/layer-juju-client.git) | juju-client | Layer for Charms which depend on Juju CLI being installed in active Model  |
| [layer-debug](https://github.com/charms/layer-debug.git) | debug | Provides a troubleshooting debug action |
| [leadership](https://git.launchpad.net/layer-leadership) | Leadership layer | Help reactive framework charms deal with Juju leadership |
| [lets-encrypt](https://github.com/cmars/layer-lets-encrypt) | lets-encrypt | Automatic Let's Encrypt registration for Juju charms, just set the fqdn |
| [lxd-proxy](https://github.com/omnivector-solutions/layer-lxd-proxy) | LXD Proxy | iptables proxy that adds and removes PREROUTING rules to ease host -> container proxying with juju |
| [memcache-client](https://github.com/omnivector-solutions/layer-memcache-client) | Memcache Client | Client layer for Memcache |
| [metrics](https://github.com/CanonicalLtd/layer-metrics) | Metrics Layer | Reactive charm layer supporting Juju metrics collection |
| [munin](https://github.com/freyes/layer-munin) | munin | munin server |
| [nagios](https://git.launchpad.net/nagios-layer) | Nagios Layer | Provide boilerplate required to relate services to the cs:nrpe subordinate |
| [nginx-passenger](https://github.com/omnivector-solutions/layer-nginx-passenger) | Nginx Passenger | Reactive layer for nginx-passenger |
| [nginx](https://github.com/battlemidget/juju-layer-nginx.git) | NGINX | NGINX layer for deploying web applications |
| [nodejs](https://github.com/battlemidget/juju-layer-node.git) | NodeJS | Runtime layer for NodeJS applications |
| [ntpmon](https://git.launchpad.net/ntpmon) | ntpmon | NTP monitoring for telegraf |
| [nvidia-cuda](https://github.com/juju-solutions/layer-nvidia-cuda) | Nvidia CUDA | Installs CUDA and Nvidia drivers when supported GPU hardware is detected |
| [openjdk](https://github.com/juju-solutions/layer-openjdk.git) | OpenJDK | OpenJDK using the java layer |
| [openstack-api](https://github.com/openstack/charm-layer-openstack-api) | OpenStack API layer | OpenStack API layer |
| [openstack-principle](https://github.com/openstack/charm-layer-openstack-principle) | OpenStack principle layer | OpenStack principle layer |
| [openstack](https://github.com/openstack/charm-layer-openstack) | OpenStack base layer | OpenStack base layer |
| [options](https://github.com/juju-solutions/layer-options.git) | options | Layer for reading options defined in layer.yaml |
| [promreg-client](https://git.launchpad.net/~prometheus-registration-developers/prometheus-registration/+git/layer-promreg-client) | promreg-client | A layer to aid in registering a target with Prometheus Registration |
| [puppet-agent](https://github.com/omnivector-solutions/layer-puppet-agent.git) | Puppet Agent | Puppet-agent layer - supports puppet 3 & 4. |
| [puppet](https://github.com/juju-solutions/layer-puppet.git) | Puppet Layer (deprecated) | Puppet layer (deprecated; use puppet-agent) |
| [ruby](https://github.com/battlemidget/juju-layer-ruby.git) | Ruby | Build layer for Ruby applications |
| [slurm](https://github.com/omnivector-solutions/layer-slurm) | slurm | Base layer for Slurm |
| [snap-action](https://github.com/lutostag/layer-snap-action.git) | snap-action | Perform snap commands via an action |
| [snap](https://git.launchpad.net/layer-snap) | Snap layer | Snap layer for installing and updating Snap packages |
| [sshproxy](https://github.com/AdamIsrael/layer-sshproxy) | sshproxy | A layer intended to ease the development of charms that need to execute commands over SSH. |
| [status](https://github.com/juju-solutions/layer-status) | Status management layer | Manage workload status in reactive charms |
| [storage](https://github.com/juju-solutions/layer-storage) | Storage | A charm layer to handle Juju attached storage devices. |
| [supervisor](https://github.com/omnivector-solutions/layer-supervisor) | Supervisor | Layer for Supervisor |
| [swarm](https://github.com/chuckbutler/layer-swarm.git) | Docker Swarm | Stand alone layer, to extend docker into a Swarm cluster participant |
| [tls-client](https://github.com/juju-solutions/layer-tls-client.git) | tls-client | A layer to handle interface:tls-certificates requires side. |
| [tls](https://github.com/juju-solutions/layer-tls) | tls | The tls charm layer creates certificates and keys for each peer unit of a charm. |
| [uwsgi](https://github.com/marcoceppi/layer-uwsgi) | uWSGI | uWSGI layer |
| [vnfproxy](https://github.com/AdamIsrael/vnfproxy.git) | vnfproxy | A layer to ease development of "proxy" charms that operate against VNF images |

<!-- /list-of-layers -->

List of Interface Layers
========================

<!-- list-of-interfaces -->

| ID | Name | Summary |
| --- | --- | --- |
| [apache-website](https://github.com/juju-solutions/interface-apache-website.git) | apache-website | Interface layer for the apache-website interface protocol |
| [arangodb](https://github.com/tengu-team/interface-arangodb.git) | arangodb | Interface layer for ArangoDB |
| [audit](https://launchpad.net/~timkuhlman/charm-layer-auditd/audit-interface) | audit | Interface for use with the auditd charm |
| [aws-integration](https://github.com/juju-solutions/interface-aws-integration.git) | aws-integration | Interface layer for connecting to the AWS integration charm |
| [azure-integration](https://github.com/juju-solutions/interface-azure-integration.git) | azure-integration | Interface layer for connecting to the Azure integration charm |
| [barbican-hsm](https://github.com/openstack/charm-interface-barbican-hsm) | barbican-hsm | Interface supporting the integration between Barbican and HSM devices |
| [basic-auth-check](https://github.com/CanonicalLtd/juju-interface-basic-auth-check) | basic-auth-check | Interface for the basic-auth-service to validate HTTP Basic-Auth credentials |
| [benchmark](https://github.com/juju-solutions/interface-benchmark.git) | benchmark | Interface layer for the benchmark protocol |
| [bgp](https://github.com/openstack/charm-interface-bgp.git) | bgp | Interface layer for exchanging BGP neighbour information between charms |
| [bind-rndc](https://github.com/openstack/charm-interface-bind-rndc) | BIND RNDC interface | BIND RNDC interface |
| [cassandra](https://git.launchpad.net/interface-cassandra) | cassandra | Cassandra database client interface |
| [ceph-admin](https://github.com/cholcombe973/juju-interface-ceph-admin) | ceph-admin | The admin interface for ceph will provide the user with the ceph admin key |
| [ceph-base](https://github.com/openstack/charm-layer-ceph-base) | Ceph Base Layer | Ceph base layer |
| [ceph-client](https://github.com/openstack-charmers/charm-interface-ceph-client) | ceph-client | Ceph Client interface |
| [ceph-mds](https://github.com/openstack/charm-interface-ceph-mds) | ceph-mds | CephFS interface to the MDS relation on ceph-mon |
| [ceph-osd](https://github.com/ChrisMacNaughton/juju-interface-ceph-osd) | ceph-osd | ceph osd relation |
| [ceph-radosgw](https://github.com/ChrisMacNaughton/juju-interface-ceph-radosgw) | ceph-radosgw | Ceph RadosGW interface |
| [ceph](https://github.com/ChrisMacNaughton/juju-interface-ceph) | ceph | ceph mon peer interface |
| [charms-ci](https://github.com/juju-solutions/interface-charms-ci.git) | charms-ci | Juju charms CI interface |
| [conda](https://github.com/omnivector-solutions/interface-conda) | Conda | Conda provides and requires interfaces |
| [conn-check](https://git.launchpad.net/~ubuntuone-hackers/conn-check/+git/interface-conn-check) | conn-check | conn-check interface |
| [consul-agent](https://github.com/ChrisMacNaughton/juju-interface-consul.git) | consul-agent | Hashicorp Consul |
| [consul](https://github.com/juju-solutions/interface-consul) | consul | Hashicorp Consul |
| [cwr-ci](https://github.com/juju-solutions/interface-cwr-ci.git) | cwr-ci | Interface for relating to Cloud Weather Report (part of the Juju CI system) |
| [db-info](https://github.com/omnivector-solutions/interface-db-info) | DB Info | Ease the process of application <-> application database creds transference. |
| [db2](https://launchpad.net/~ibmcharmers/interface-ibm-db2/trunk) | db2 | This interface layer handles the communication between  IBM DB2 and Consumer charms. |
| [dbname](https://github.com/omnivector-solutions/interface-dbname.git) | DB Name | Interface to coordinate database name between applications. |
| [designate](https://github.com/openstack-charmers/charm-interface-designate) | designate | Designate DNS as a Service interface |
| [dfs-slave](https://github.com/juju-solutions/interface-dfs-slave.git) | dfs-slave | Interface layer for the DataNode <-> NameNode protocol |
| [dfs](https://github.com/juju-solutions/interface-dfs.git) | dfs | Interface layer for the hdfs interface protocol |
| [dm-node](https://code.launchpad.net/~ibmcharmers/interface-ibm-dm-node/trunk) | dm-node | This interface handles the comunication between IBM WAS ND DM and IBM WAS ND Node charms |
| [docker-image-host](https://github.com/tengu-team/interface-docker-image-host) | docker-image-host | Interface to send image to docker host |
| [dockerhost](https://github.com/juju-solutions/interface-dockerhost) | dockerhost | Docker connection information for a unit |
| [druid-config](https://gitlab.com/spiculedata/juju/druid-config-relation) | Druid Configuration | Configuration layer for Spicule's Druid charms. |
| [elastic-beats](https://github.com/juju-solutions/interface-elastic-beats) | elastic-beats | Interface for elastic beats |
| [elasticsearch](http://github.com/juju-solutions/interface-elasticsearch ) | elasticsearch | Interface to connect with elasticsearch. |
| [etcd-proxy](https://github.com/juju-solutions/interface-etcd-proxy) | etcd-proxy | Do you need etcd as a read/readwrite proxy to a cluster? use this interface. |
| [etcd](https://github.com/juju-solutions/interface-etcd) | etcd | Interface for relating to etcd |
| [flume-agent](https://github.com/juju-solutions/interface-flume-agent.git) | flume-agent | Interface layer for communication between Apache Flume charms |
| [gcp-integration](https://github.com/juju-solutions/interface-gcp-integration.git) | gcp-integration | Interface layer for connecting to the GCP integration charm |
| [giraph](https://github.com/juju-solutions/interface-giraph) | giraph | This interface handles the communication between Apache Giraph and its clients |
| [gluster-fuse](https://github.com/cholcombe973/juju-interface-gluster-fuse) | gluster-fuse | Distributed posix storage provided by GlusterFS |
| [gluster-nfs](https://github.com/cholcombe973/juju-interface-gluster-client) | gluster-nfs | Scale out NFS provided by GlusterFS |
| [gluster-peer](https://github.com/wolsen/charm-interface-gluster-peer) | gluster-peer | Peer interface for glusterfs nodes |
| [gnocchi](https://github.com/openstack-charmers/charm-interface-gnocchi) | gnocchi | Gnocchi Metrics Service interface |
| [gpfs](https://code.launchpad.net/~ibmcharmers/interface-ibm-gpfs/trunk) | gpfs | Interface layer between IBM Spectrum Scale Manager and IBM Spectrum Scale client as well as peer communication among manager/client units |
| [grafana-source](https://git.launchpad.net/interface-grafana-source) | grafana-source | Grafana source |
| [hacluster](https://github.com/openstack/charm-interface-hacluster.git) | hacluster | hacluster interface for relations with hacluster subordinate charm |
| [hadoop-plugin](https://github.com/juju-solutions/interface-hadoop-plugin.git) | hadoop-plugin | Interface for relating to Apache Hadoop |
| [hadoop-rest](https://github.com/juju-solutions/interface-hadoop-rest) | hadoop-rest | Interface layer for connecting to hadoop-plugin without installation |
| [hbase-quorum](https://github.com/juju-solutions/interface-hbase-quorum.git) | hbase quorum | This interface layer handles the communication among Apache HBase peers |
| [hbase](https://github.com/juju-solutions/interface-hbase.git) | hbase | This interface layer handles the communication between Apache HBase and its clients |
| [hive](https://github.com/juju-solutions/interface-hive.git) | hive | Interface for relating to Apache Hive |
| [http](https://github.com/juju-solutions/interface-http.git) | http | HTTP Relation Stub |
| [https](https://code.launchpad.net/~ibmcharmers/interface-https/trunk) | https |  Basic HTTPS interface |
| [ibm-db2](https://launchpad.net/~ibmcharmers/interface-ibm-db2/trunk) | ibm-db2 | This interface layer handles the communication between  IBM DB2 and Consumer charms. |
| [ibm-mq](https://code.launchpad.net/~ibmcharmers/interface-ibm-mq/trunk) | ibm-mq | This interface handles the communication between IBM MQ and other consumer charms. |
| [ibm-wxs](https://launchpad.net/~ibmcharmers/interface-ibm-wxs/trunk) | ibm-wxs | This interface layer handles the communication between  IBM WXS Catalog charm and other consumer charms, such as IBM WXS Container and IBM WXS Client |
| [ignite-hadoop](https://github.com/juju-solutions/interface-ignite-hadoop) | ignite-hadoop | Minimal interface layer for connecting Apache Ignite-Hadoop to Apache Hadoop slave |
| [influxdb-api](https://github.com/ChrisMacNaughton/interface-influxdb-api.git) | influxdb-api | InfluxDB Query Interface |
| [java](https://github.com/juju-solutions/interface-java.git) | java | Interface for relating to subordinate charms providing a Java runtime or JDK |
| [jdbc](https://gitlab.com/spiculedata/juju/jdbc-interface.git) | jdbc | JDBC interface for generic connectivity across databases |
| [jenkins-extension](https://github.com/juju-solutions/interface-jenkins-extension.git) | jenkins-extension | Admin interface to the jenkins master |
| [jenkins-slave](https://github.com/freeekanayaka/interface-jenkins-slave.git) | jenkins-slave | Communication between a Jenkins master and a Jenkins slave |
| [jenkins-zuul](https://github.com/freeekanayaka/interface-jenkins-zuul.git) | jenkins-zuul | communication between a Jenkins master and Zuul Jenkins via the zuul interface |
| [juju-info](https://github.com/juju-solutions/interface-juju-info.git) | juju-info | Implied interface for subordinates with special behavior. This is not a substitute for a proper relationship interface.  |
| [kafka](https://github.com/juju-solutions/interface-kafka.git) | kafka | Interface layer for communication between Kafka and its clients |
| [kapacitor](https://github.com/tengu-team/interface-kapacitor.git) | kapacitor | Interface layer for Kapacitor |
| [keystone-admin](https://github.com/openstack/charm-interface-keystone-admin) | keystone-admin | keystone-admin:identity-admin interface to use shared admin API credentials |
| [keystone-credentials](https://github.com/openstack/charm-interface-keystone-credentials) | keystone-credentials | keystone-credentials: Interface for integrating with Keystone identity credentials |
| [keystone-domain-backend](https://github.com/openstack-charmers/charm-interface-keystone-domain-backend) | keystone-domain-backend | Interface for integration of subordinate charms providing domain specific identity backends |
| [keystone-fid-service-provider](https://github.com/dshcherb/charm-interface-keystone-fid-service-provider) | keystone-fid-service-provider | An interface to connect a federated identity provider to the Keystone charm |
| [keystone](https://github.com/openstack/charm-interface-keystone) | keystone | Keystone interface |
| [kube-control](https://github.com/juju-solutions/interface-kube-control.git) | kube-control | master-worker control interface for Kubernetes |
| [kube-dns](https://github.com/juju-solutions/interface-kube-dns.git) | kube-dns | Kubernetes DNS Details |
| [kubernetes-cni](https://github.com/juju-solutions/interface-kubernetes-cni) | kubernetes-cni | Interface for relating various CNI implementations |
| [limeds](https://github.com/tengu-team/interface-limeds) | limeds | Interface to connect to LimeDS |
| [livy](https://gitlab.com/spiculedata/juju/livy-relation.git) | Apache Livy relation | Relation to connect a charm to Apache Livy. |
| [local-monitors](https://github.com/cmars/local-monitors-interface) | local-monitors | relation for registering nagios checks |
| [logstash-client](https://github.com/juju-solutions/interface-logstash-client) | logstash-client | Interface for connecting with logstash based systems. |
| [mahout](https://github.com/juju-solutions/interface-mahout) | mahout | This interface layer handles the communication between Apache Mahout and its clients |
| [manila-plugin](https://github.com/openstack/charm-interface-manila-plugin) | manila-plugin | manila-plugin: configuration plugin to allow manila plugins to configure the manila service |
| [mapred-slave](https://github.com/juju-solutions/interface-mapred-slave.git) | mapred-slave | Interface layer for the NodeManager <-> ResourceManager protocol |
| [mapred](https://github.com/juju-solutions/interface-mapred.git) | mapred | Interface for the YARN client protocol |
| [memcache](https://github.com/omnivector-solutions/interface-memcache.git) | Memcache | Interface for relating memcache. |
| [midonet-api](https://github.com/celebdor/interface-midonet-api.git) | MidoNet API | MidoNet API interface between provider and consuming charms |
| [mongodb-cluster](https://github.com/tkuhlman/juju-relation-mongodb) | mongodb-cluster | relation to connect to a mongo database cluster |
| [mongodb](https://github.com/cloud-green/juju-relation-mongodb) | mongodb | relation to connect to a mongo database |
| [monitor](https://github.com/juju-solutions/interface-monitor.git) | monitor | This interface layer for monitor protocol |
| [mount](https://github.com/juju-solutions/interface-mount.git) | mount | Interface layer for connecting mounts to a charm such as NFS |
| [munin-node](https://github.com/freyes/interface-munin-node) | munin-node | munin-node relation |
| [munin](https://github.com/freyes/interface-munin) | munin | munin relation |
| [mysql-root](https://github.com/juju-solutions/interface-mysql-root.git) | mysql-root | Administrative MySQL interface with admin access granted to connected applications |
| [mysql-shared](https://github.com/openstack/charm-interface-mysql-shared) | mysql-shared | MySQL Shared Database interface |
| [mysql](https://github.com/johnsca/juju-relation-mysql.git) | mysql | Standard MySQL interface with generated, per-service databases |
| [namenode-cluster](https://github.com/juju-solutions/interface-namenode-cluster.git) | namenode-cluster | Interface layer for running Apache Hadoop NameNode as HA |
| [neutron-plugin-api-subordinate](https://github.com/openstack/charm-interface-neutron-plugin-api-subordinate) | neutron-plugin-api-subordinate | This interface is used for a charm to send configuration information to the neutron-api principle charm and request a restart of a service managed by that charm. |
| [neutron-plugin-zlmao](https://github.com/openstack/charm-interface-neutron-plugin) | neutron-plugin | Interface for intergrating Neutron SDN with the nova-compute charm |
| [neutron-plugin](https://github.com/openstack/charm-interface-neutron-plugin) | neutron-plugin | Interface for intergrating Neutron SDN with the nova-compute charm |
| [nfsstorage](https://launchpad.net/~ibmcharmers/interface-ibm-nfsstorage/trunk) | nfsstorage | This interface layer handles the communication between LSF/Spectrum Symphony Storage which is acting as a NFS Server and NFS Clients like Platform LSF Master, Spectrum Symphony Master. |
| [nginx-stats](https://github.com/silph-io/interface-nginx-stats) | NGINX Stats | NGINX stats/status protocol |
| [nrpe-external-master](https://github.com/cmars/nrpe-external-master-interface) | nrpe-external-master | relation for registering nagios checks |
| [odl-controller-api](https://github.com/openstack/charm-interface-odl-controller-api) | odl-controller-api | Interface for intergrating with an OpenDayLight Controller RESTful API |
| [oozie](https://gitlab.com/spiculedata/juju/oozie-interface.git) | oozie | Connection for oozie to consumers |
| [openstack-ha](https://github.com/openstack/charm-interface-openstack-ha) | openstack-ha | Interface for managing information with peers in the same OpenStack service |
| [openstack-integration](https://github.com/juju-solutions/interface-openstack-integration.git) | openstack-integration | Interface layer for connecting to the OpenStack integrator charm |
| [opentsdb](https://github.com/tengu-team/interface-opentsdb.git) | opentsdb | Interface layer for OpenTSDB. |
| [ovsdb-manager](https://github.com/openstack/charm-interface-ovsdb-manager) | ovsdb-manager | Interface for relating to the OVSDB manager aspect of OpenDayLight SDN |
| [panko](https://github.com/openstack-charmers/charm-interface-panko) | panko | Panko Event Service interface |
| [peer-discovery](https://github.com/tbaumann/charm-interface-peer-discovery) | peer-discovery | [proposal] simple interface to discover all peers of a charm through peer relation |
| [pgsql](https://git.launchpad.net/interface-pgsql) | pgsql | Postgresql database client interface |
| [platformmaster](https://launchpad.net/~ibmcharmers/interface-ibm-platformmaster/trunk) | platformmaster | This interface layer handles the communication between Platform Master (like IBM Platform LSF, IBM Spectrum Symphony) and Platform Server/Nodes. |
| [prometheus-rules](https://github.com/CanonicalBootStack/interface-prometheus-rules.git) | prometheus-rules | Relation Stub to export Prometheus alerting rules |
| [prometheus](https://git.launchpad.net/interface-prometheus) | prometheus | Prometheus target interface |
| [public-address](https://github.com/juju-solutions/interface-public-address) | public-address | Simple relation that provides the providers public-address and a port |
| [rabbitmq](https://github.com/openstack/charm-interface-rabbitmq) | rabbitmq | RabbitMQ AMQP interface |
| [redis](https://github.com/omnivector-solutions/interface-redis) | redis | Interface for relating to redis |
| [rsyslog](https://bazaar.launchpad.net/~canonical-sysadmins/canonical-is-charms/layer-rsyslog/files) | Rsyslog layer | This rsyslog layer will enable rsyslog and enable building additional logging configuration. |
| [sdn-plugin](https://github.com/juju-solutions/interface-sdn-plugin) | sdn-plugin | An abstraction of common configurations for SDN providers, to be consumed by charms |
| [service-control](https://github.com/openstack/charm-interface-service-control) | service-control | This interface is used for a charm to request a restart of a service managed by another charm. |
| [slurm-cluster](https://github.com/omnivector-solutions/interface-slurm-cluster) | slurm-cluster | Interface layer for Slurm |
| [solr](https://github.com/buggtb/interface-solr) | solr | Solr Charm Interface |
| [spark-quorum](https://github.com/juju-solutions/interface-spark-quorum.git) | spark quorum | This interface layer handles the communication among Apache Spark peers |
| [spark](https://github.com/juju-solutions/interface-spark.git) | spark | Interface layer for the spark interface protocol |
| [spectrum-scale-client](https://code.launchpad.net/~ibmcharmers/interface-spectrum-scale-client/trunk) | spectrum-scale-client | Basic interface required for communication between Spectrum Scale client and IBM Cinder SpectrumScale (driver for gpfs) |
| [syslog](https://github.com/juju-solutions/interface-syslog.git) | syslog | Interface layer for the syslog protocol |
| [tls-certificates](https://github.com/juju-solutions/interface-tls-certificates) | tls-certificates | An interface for exchanging tls certificates using provides and requres relations. |
| [tls](https://github.com/juju-solutions/interface-tls) | tls | The TLS interface provides a peering relationship to exchange certificates and CSR's. |
| [vault-kv](https://github.com/openstack-charmers/charm-interface-vault-kv.git) | vault-kv | Interface layer for the vault-kv protocol |
| [vault](https://github.com/ChrisMacNaughton/juju-interface-vault.git) | vault | Hashicorp Vault omterface |
| [was-ihs](https://code.launchpad.net/~ibmcharmers/interface-ibm-was-ihs/trunk) | was-ihs | This Interface handles the communication between IBM WAS Base/IBM WAS ND and IBM Http Server |
| [was-nd](https://code.launchpad.net/~ibmcharmers/interface-ibm-was-nd/trunk) | was-nd | This interface handles the communication between IBM WAS ND DM and other consumer charms. |
| [websso-fid-service-provider](https://github.com/dshcherb/charm-interface-websso-fid-service-provider) | websso-fid-service-provider | An interface to connect a federated identity provider to OpenStack dashboard charm |
| [weebl](https://github.com/autonomouse/interface-weebl) | weebl | Interface for relating to the OIL dashboard (Weebl) |
| [wsgi](https://git.launchpad.net/~ubuntuone-hackers/charms/+source/interface-wsgi) | wsgi | Basic WSGI interface |
| [zeppelin](https://github.com/juju-solutions/interface-zeppelin) | zeppelin | Interface layer for interacting with charms for Apache Zeppelin |
| [zookeeper-quorum](https://github.com/juju-solutions/interface-zookeeper-quorum.git) | zookeeper quorum | This interface layer handles the communication among Apache Zookeeper peers |
| [zookeeper](https://github.com/juju-solutions/interface-zookeeper.git) | zookeeper | This interface layer handles the communication between Apache Zookeeper and its clients |

<!-- /list-of-interfaces -->
