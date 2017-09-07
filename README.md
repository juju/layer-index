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
| [apache2](https://github.com/jamesbeedy/layer-apache2) | Apache2 | Reactive layer for Apache webserver |
| [apt](https://git.launchpad.net/layer-apt) | Apt layer | Easily deal with apt sources and deb packages |
| [barbican-client](https://github.com/jamesbeedy/juju-layer-barbican-client) | Barbican Client | Reactive layer to help pull secrets from barbican |
| [basic](https://github.com/juju-solutions/layer-basic.git) | Basic Layer | Base layer for charms with the Reactive framework |
| [beats-base](https://github.com/juju-solutions/layer-beats-base) | Beats Base | Base layer for Elastic Beats |
| [bigtop-base](https://github.com/juju-solutions/layer-apache-bigtop-base.git) | Apache Bigtop Base Layer | Base layer for charms needing Apache Bigtop  |
| [buildpacks](https://git.launchpad.net/~bcsaller/charms/+source/buildpacks) | Buildpacks | Experimental layer for using buildpacks to generate Charmed applications |
| [ceph-base](https://github.com/ChrisMacNaughton/layer-ceph-base) | EXPERIMENTAL Ceph Base Layer | EXPERIMENTAL Ceph base layer |
| [ceph-basic](https://github.com/ChrisMacNaughton/layer-ceph-basic) | EXPERIMENTAL ceph-basic | EXPERIMENTAL ceph-basic layer |
| [ceph-mon](https://github.com/ChrisMacNaughton/juju-layer-ceph-mon) | EXPERIMENTAL Ceph Mon layer | EXPERIMENTAL Ceph Mon layer |
| [charmscaler-base](https://github.com/elastisys/layer-charmscaler-base) | Charmscaler Base | Charmscaler base layer |
| [composer](https://github.com/jamesbeedy/juju-layer-composer) | PHP Composer | Reactive layer for php composer |
| [consul-base](https://github.com/jamesbeedy/layer-consul-base) | Consul Base | Reactive base layer for consul |
| [coordinator](https://git.launchpad.net/layer-coordinator ) | Coordinator Layer | Coordinate operations between units in a service, such as rolling restarts. |
| [debug](https://github.com/charms/layer-debug.git) | debug | Provides a troubleshooting debug action |
| [django](https://github.com/marcoceppi/layer-django.git) | Django | Django / GUNICORN |
| [docker](https://github.com/juju-solutions/layer-docker.git) | Docker | Layer to deliver and install Docker on Ubuntu, Debian, Centos hosts. |
| [elasticsearch-base](https://github.com/jamesbeedy/juju-layer-elasticsearch-base) | Elasticsearch Base | Base layer for elasticsearch |
| [elixir](https://github.com/battlemidget/juju-layer-elixir.git) | Elixir | Runtime layer for Elixir applications |
| [flannel](https://github.com/juju-solutions/layer-flannel) | Flannel | Flannel Overlay Network layer for docker |
| [flask](https://github.com/IBCNServices/layer-flask) | Flask | Layer to create Flask webservers running on nginx |
| [git-deploy](https://github.com/jamesbeedy/layer-git-deploy.git) | Git Deploy | Layer to aid with deploying code from github |
| [gitlab](https://github.com/jamesbeedy/layer-gitlab.git) | Gitlab Layer | Reactive layer for gitlab |
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
| [java](https://github.com/jamesbeedy/juju-layer-java) | Oracle Java | Juju layer for Oracle Java |
| [jenkins-workspace](https://github.com/juju-solutions/layer-jenkins-workspace) | Jenkins Workspace | Configure Jenkins with workspace snapshots |
| [jenkins](https://github.com/jenkinsci/jenkins-charm.git) | jenkins | Juju charm to deploy and scale Jenkins  |
| [juju-client](https://github.com/tengu-team/layer-juju-client.git) | juju-client | Layer for Charms which depend on Juju CLI being installed in active Model  |
| [layer-debug](https://github.com/charms/layer-debug.git) | debug | Provides a troubleshooting debug action |
| [layer-gitlab](https://github.com/jamesbeedy/layer-gitlab.git) | Gitlab Layer | Reactive layer for gitlab |
| [leadership](https://git.launchpad.net/layer-leadership) | Leadership layer | Help reactive framework charms deal with Juju leadership |
| [lets-encrypt](https://github.com/cmars/layer-lets-encrypt) | lets-encrypt | Automatic Let's Encrypt registration for Juju charms, just set the fqdn |
| [lxd-proxy](https://github.com/jamesbeedy/layer-lxd-proxy) | LXD-Proxy | iptables proxy that adds and removes PREROUTING rules to ease host -> container proxying with juju |
| [metrics](https://github.com/CanonicalLtd/layer-metrics) | Metrics Layer | Reactive charm layer supporting Juju metrics collection |
| [munin](https://github.com/freyes/layer-munin) | munin | munin server |
| [nagios](https://git.launchpad.net/nagios-layer) | Nagios Layer | Provide boilerplate required to relate services to the cs:nrpe subordinate |
| [nginx-passenger](https://github.com/jamesbeedy/layer-nginx-passenger) | Nginx-Passenger | Reactive layer for nginx-passenger |
| [nginx](https://github.com/battlemidget/juju-layer-nginx.git) | NGINX | NGINX layer for deploying web applications |
| [nodejs](https://github.com/battlemidget/juju-layer-node.git) | NodeJS | Runtime layer for NodeJS applications |
| [ntpmon](https://git.launchpad.net/ntpmon) | ntpmon | NTP monitoring for telegraf |
| [nvidia-cuda](https://github.com/juju-solutions/layer-nvidia-cuda) | Nvidia CUDA | Installs CUDA and Nvidia drivers when supported GPU hardware is detected |
| [openjdk](https://github.com/juju-solutions/layer-openjdk.git) | OpenJDK | OpenJDK using the java layer |
| [openstack-api](https://github.com/openstack/charm-layer-openstack-api) | OpenStack API layer | OpenStack API layer |
| [openstack-principle](https://github.com/openstack/charm-layer-openstack-principle) | OpenStack principle layer | OpenStack principle layer |
| [openstack](https://github.com/openstack/charm-layer-openstack) | OpenStack base layer | OpenStack base layer |
| [phalcon](https://github.com/jamesbeedy/layer-phalcon) | Phalcon | Reactive layer for installing and configuring Phalcon php web framework |
| [postfix](https://github.com/jamesbeedy/layer-postfix.git) | Postfix | Reactive layer for postfix MTA |
| [promreg-client](https://git.launchpad.net/~timkuhlman/prometheus-registration/+git/layer-promreg-client) | promreg-client | A layer to aid in registering a target with Prometheus Registration |
| [puppet-agent](https://github.com/jamesbeedy/layer-puppet-agent.git) | Puppet-agent | Puppet-agent layer - supports puppet 3 & 4. |
| [puppet-base](https://github.com/jamesbeedy/layer-puppet-base.git) | puppet-base | Base layer for puppet4 |
| [puppet](https://github.com/juju-solutions/layer-puppet.git) | Puppet Layer (deprecated) | Puppet layer (deprecated; use puppet-agent) |
| [ruby](https://github.com/battlemidget/juju-layer-ruby.git) | Ruby | Build layer for Ruby applications |
| [snap-action](https://github.com/lutostag/layer-snap-action.git) | snap-action | Perform snap commands via an action |
| [snap](https://git.launchpad.net/layer-snap) | Snap layer | Snap layer for installing and updating Snap packages |
| [sshproxy](https://github.com/AdamIsrael/layer-sshproxy) | sshproxy | A layer intended to ease the development of charms that need to execute commands over SSH. |
| [storage](https://github.com/juju-solutions/layer-storage) | Storage | A charm layer to handle Juju attached storage devices. |
| [supervisor](https://github.com/jamesbeedy/layer-supervisor) | Supervisor | Layer for Supervisor |
| [swarm](https://github.com/chuckbutler/layer-swarm.git) | Docker Swarm | Stand alone layer, to extend docker into a Swarm cluster participant |
| [tls-client](https://github.com/juju-solutions/layer-tls-client.git) | tls-client | A layer to handle interface:tls-certificates requires side. |
| [tls](https://github.com/juju-solutions/layer-tls) | tls | The tls charm layer creates certificates and keys for each peer unit of a charm. |
| [uwsgi](https://github.com/marcoceppi/layer-uwsgi) | uWSGI | uWSGI layer |
| [vnfproxy](https://github.com/AdamIsrael/vnfproxy.git) | vnfproxy | A layer to ease development of "proxy" charms that operate against VNF images |
| [zabbix-base](https://github.com/jamesbeedy/layer-zabbix-base) | zabbix-base | Reactive base layer for zabbix charms |
<!-- /list-of-layers -->

List of Interface Layers
========================

<!-- list-of-interfaces -->
| ID | Name | Summary |
| --- | --- | --- |
| [apache-website](https://github.com/juju-solutions/interface-apache-website.git) | apache-website | Interface layer for the apache-website interface protocol |
| [audit](https://launchpad.net/~timkuhlman/charm-layer-auditd/audit-interface) | audit | Interface for use with the auditd charm |
| [barbican-hsm](https://github.com/openstack/charm-interface-barbican-hsm) | barbican-hsm | Interface supporting the integration between Barbican and HSM devices |
| [basic-auth-check](https://github.com/CanonicalLtd/juju-interface-basic-auth-check) | basic-auth-check | Interface for the basic-auth-service to validate HTTP Basic-Auth credentials |
| [beanstalkd](https://github.com/jamesbeedy/juju-interface-beanstalkd) | beanstalkd | Reactive provides and requires interfaces for beanstalkd |
| [benchmark](https://github.com/juju-solutions/interface-benchmark.git) | benchmark | Interface layer for the benchmark protocol |
| [bind-rndc](https://github.com/openstack/charm-interface-bind-rndc) | BIND RNDC interface | BIND RNDC interface |
| [ceph-admin](https://github.com/cholcombe973/juju-interface-ceph-admin) | ceph-admin | The admin interface for ceph will provide the user with the ceph admin key |
| [ceph-base](https://github.com/openstack/charm-layer-ceph-base) | Ceph Base Layer | Ceph base layer |
| [ceph-client](https://github.com/openstack-charmers/charm-interface-ceph-client) | ceph-client | Ceph Client interface |
| [ceph-mds](https://github.com/openstack/charm-interface-ceph-mds) | ceph-mds | CephFS interface to the MDS relation on ceph-mon |
| [ceph-osd](https://github.com/ChrisMacNaughton/juju-interface-ceph-osd) | ceph-osd | ceph osd relation |
| [ceph-radosgw](https://github.com/ChrisMacNaughton/juju-interface-ceph-radosgw) | ceph-radosgw | Ceph RadosGW interface |
| [ceph](https://github.com/ChrisMacNaughton/juju-interface-ceph) | ceph | ceph mon peer interface |
| [charms-ci](https://github.com/juju-solutions/interface-charms-ci.git) | charms-ci | Juju charms CI interface |
| [conn-check](https://git.launchpad.net/~ubuntuone-hackers/conn-check/+git/interface-conn-check) | conn-check | conn-check interface |
| [consul-agent](https://github.com/ChrisMacNaughton/juju-interface-consul.git) | consul-agent | Hashicorp Consul |
| [consul](https://github.com/juju-solutions/interface-consul) | consul | Hashicorp Consul |
| [cwr-ci](https://github.com/juju-solutions/interface-cwr-ci.git) | cwr-ci | Interface for relating to Cloud Weather Report (part of the Juju CI system) |
| [db2](https://launchpad.net/~ibmcharmers/interface-ibm-db2/trunk) | db2 | This interface layer handles the communication between  IBM DB2 and Consumer charms. |
| [dbname](https://github.com/jamesbeedy/juju-interface-dbname.git) | dbname | Interface to coordinate database name between applications. |
| [dfs-slave](https://github.com/juju-solutions/interface-dfs-slave.git) | dfs-slave | Interface layer for the DataNode <-> NameNode protocol |
| [dfs](https://github.com/juju-solutions/interface-dfs.git) | dfs | Interface layer for the hdfs interface protocol |
| [dm-node](https://code.launchpad.net/~ibmcharmers/interface-ibm-dm-node/trunk) | dm-node | This interface handles the comunication between IBM WAS ND DM and IBM WAS ND Node charms |
| [docker-image-host](https://github.com/tengu-team/interface-docker-image-host) | docker-image-host | Interface to send image to docker host |
| [dockerhost](https://github.com/juju-solutions/interface-dockerhost) | dockerhost | Docker connection information for a unit |
| [elastic-beats](https://github.com/juju-solutions/interface-elastic-beats) | elastic-beats | Interface for elastic beats |
| [elasticsearch-stats](https://github.com/jamesbeedy/interface-elasticsearch-stats.git) | Elasticsearch Stats | Interface for integrating with metrics gathering layers  |
| [elasticsearch](http://github.com/juju-solutions/interface-elasticsearch ) | elasticsearch | Interface to connect with elasticsearch. |
| [etcd-proxy](https://github.com/juju-solutions/interface-etcd-proxy) | etcd-proxy | Do you need etcd as a read/readwrite proxy to a cluster? use this interface. |
| [etcd](https://github.com/juju-solutions/interface-etcd) | etcd | Interface for relating to etcd |
| [flume-agent](https://github.com/juju-solutions/interface-flume-agent.git) | flume-agent | Interface layer for communication between Apache Flume charms |
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
| [jenkins-extension](https://github.com/juju-solutions/interface-jenkins-extension.git) | jenkins-extension | Admin interface to the jenkins master |
| [jenkins-slave](https://github.com/freeekanayaka/interface-jenkins-slave.git) | jenkins-slave | Communication between a Jenkins master and a Jenkins slave |
| [jenkins-zuul](https://github.com/freeekanayaka/interface-jenkins-zuul.git) | jenkins-zuul | communication between a Jenkins master and Zuul Jenkins via the zuul interface |
| [juju-info](https://github.com/juju-solutions/interface-juju-info.git) | juju-info | Implied interface for subordinates with special behavior. This is not a substitute for a proper relationship interface.  |
| [kafka](https://github.com/juju-solutions/interface-kafka.git) | kafka | Interface layer for communication between Kafka and its clients |
| [keystone-admin](https://git.launchpad.net/~canonical-is/charms/+source/interface-keystone-admin) | keystone-admin | keystone-admin:identity-admin interface to use shared admin API credentials |
| [keystone-credentials](https://github.com/openstack/charm-interface-keystone-credentials) | keystone-credentials | keystone-credentials: Interface for integrating with Keystone identity credentials |
| [keystone-domain-backend](https://github.com/openstack-charmers/charm-interface-keystone-domain-backend) | keystone-domain-backend | Interface for integration of subordinate charms providing domain specific identity backends |
| [keystone](https://github.com/openstack/charm-interface-keystone) | keystone | Keystone interface |
| [kube-control](https://github.com/juju-solutions/interface-kube-control.git) | kube-control | master-worker control interface for Kubernetes |
| [kube-dns](https://github.com/juju-solutions/interface-kube-dns.git) | kube-dns | Kubernetes DNS Details |
| [kubernetes-cni](https://github.com/juju-solutions/interface-kubernetes-cni) | kubernetes-cni | Interface for relating various CNI implementations |
| [limeds](https://github.com/tengu-team/interface-limeds) | limeds | Interface to connect to LimeDS |
| [local-monitors](https://github.com/cmars/local-monitors-interface) | local-monitors | relation for registering nagios checks |
| [logstash-client](https://github.com/juju-solutions/interface-logstash-client) | logstash-client | Interface for connecting with logstash based systems. |
| [mahout](https://github.com/juju-solutions/interface-mahout) | mahout | This interface layer handles the communication between Apache Mahout and its clients |
| [manila-plugin](https://github.com/openstack/charm-interface-manila-plugin) | manila-plugin | manila-plugin: configuration plugin to allow manila plugins to configure the manila service |
| [mapred-slave](https://github.com/juju-solutions/interface-mapred-slave.git) | mapred-slave | Interface layer for the NodeManager <-> ResourceManager protocol |
| [mapred](https://github.com/juju-solutions/interface-mapred.git) | mapred | Interface for the YARN client protocol |
| [memcache](https://github.com/jamesbeedy/interface-memcache.git) | memcache | Interface for relating memcache. |
| [midonet-api](https://github.com/celebdor/interface-midonet-api.git) | MidoNet API | MidoNet API interface between provider and consuming charms |
| [mongodb-cluster](https://github.com/tkuhlman/juju-relation-mongodb) | mongodb-cluster | relation to connect to a mongo database cluster |
| [mongodb](https://github.com/cloud-green/juju-relation-mongodb) | mongodb | relation to connect to a mongo database |
| [monitor](https://github.com/juju-solutions/interface-monitor.git) | monitor | This interface layer for monitor protocol |
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
| [openstack-ha](https://github.com/openstack/charm-interface-openstack-ha) | openstack-ha | Interface for managing information with peers in the same OpenStack service |
| [ovsdb-manager](https://github.com/openstack/charm-interface-ovsdb-manager) | ovsdb-manager | Interface for relating to the OVSDB manager aspect of OpenDayLight SDN |
| [panko](https://github.com/openstack-charmers/charm-interface-panko) | panko | Panko Event Service interface |
| [peer-discovery](https://github.com/tbaumann/charm-interface-peer-discovery) | peer-discovery | [proposal] simple interface to discover all peers of a charm through peer relation |
| [pgsql](https://git.launchpad.net/interface-pgsql) | pgsql | Postgresql database client interface |
| [platformmaster](https://launchpad.net/~ibmcharmers/interface-ibm-platformmaster/trunk) | platformmaster | This interface layer handles the communication between Platform Master (like IBM Platform LSF, IBM Spectrum Symphony) and Platform Server/Nodes. |
| [postgresql-stats](https://github.com/jamesbeedy/interface-postgresql-stats.git) | Postgresql Stats | Interface for integrating with metrics gathering layers |
| [prometheus](https://github.com/tasdomas/juju-interface-prometheus.git) | prometheus | Prometheus target interface |
| [public-address](https://github.com/juju-solutions/interface-public-address) | public-address | Simple relation that provides the providers public-address and a port |
| [rabbitmq](https://github.com/openstack/charm-interface-rabbitmq) | rabbitmq | RabbitMQ AMQP interface |
| [redis-stats](https://github.com/jamesbeedy/interface-redis-stats.git) | Redis Stats | Interface to be used for integration with metrics gathering layers |
| [redis](https://github.com/jamesbeedy/interface-redis) | redis | Interface for relating to redis |
| [rsyslog](https://bazaar.launchpad.net/~canonical-sysadmins/canonical-is-charms/layer-rsyslog/files) | Rsyslog layer | This rsyslog layer will enable rsyslog and enable building additional logging configuration. |
| [sdn-plugin](https://github.com/juju-solutions/interface-sdn-plugin) | sdn-plugin | An abstraction of common configurations for SDN providers, to be consumed by charms |
| [service-control](https://github.com/openstack/charm-interface-service-control) | service-control | This interface is used for a charm to request a restart of a service managed by another charm. |
| [solr](https://github.com/buggtb/interface-solr) | solr | Solr Charm Interface |
| [spark-quorum](https://github.com/juju-solutions/interface-spark-quorum.git) | spark quorum | This interface layer handles the communication among Apache Spark peers |
| [spark](https://github.com/juju-solutions/interface-spark.git) | spark | Interface layer for the spark interface protocol |
| [spectrum-scale-client](https://code.launchpad.net/~ibmcharmers/interface-spectrum-scale-client/trunk) | spectrum-scale-client | Basic interface required for communication between Spectrum Scale client and IBM Cinder SpectrumScale (driver for gpfs) |
| [syslog](https://github.com/juju-solutions/interface-syslog.git) | syslog | Interface layer for the syslog protocol |
| [tls-certificates](https://github.com/juju-solutions/interface-tls-certificates) | tls-certificates | An interface for exchanging tls certificates using provides and requres relations. |
| [tls](https://github.com/juju-solutions/interface-tls) | tls | The TLS interface provides a peering relationship to exchange certificates and CSR's. |
| [vault](https://github.com/ChrisMacNaughton/juju-interface-vault.git) | vault | Hashicorp Vault omterface |
| [was-ihs](https://code.launchpad.net/~ibmcharmers/interface-ibm-was-ihs/trunk) | was-ihs | This Interface handles the communication between IBM WAS Base/IBM WAS ND and IBM Http Server |
| [was-nd](https://code.launchpad.net/~ibmcharmers/interface-ibm-was-nd/trunk) | was-nd | This interface handles the communication between IBM WAS ND DM and other consumer charms. |
| [weebl](https://github.com/autonomouse/interface-weebl) | weebl | Interface for relating to the OIL dashboard (Weebl) |
| [wsgi](https://git.launchpad.net/~ubuntuone-hackers/charms/+source/interface-wsgi) | wsgi | Basic WSGI interface |
| [zeppelin](https://github.com/juju-solutions/interface-zeppelin) | zeppelin | Interface layer for interacting with charms for Apache Zeppelin |
| [zookeeper-quorum](https://github.com/juju-solutions/interface-zookeeper-quorum.git) | zookeeper quorum | This interface layer handles the communication among Apache Zookeeper peers |
| [zookeeper](https://github.com/juju-solutions/interface-zookeeper.git) | zookeeper | This interface layer handles the communication between Apache Zookeeper and its clients |
<!-- /list-of-interfaces -->