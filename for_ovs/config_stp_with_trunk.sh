#! /bin/bash

for i in {1..9}
do
  ovs-ofctl add-flow s$i action=NORMAL
  ovs-vsctl set bridge s$i stp_enable=true
done

# vlan 9
ovs-vsctl set port s1-eth1 tag=9
ovs-vsctl set port s2-eth2 tag=9
ovs-vsctl set port s4-eth2 tag=9
ovs-vsctl set port s5-eth3 tag=9

# vlan 10
ovs-vsctl set port s5-eth4 tag=10
ovs-vsctl set port s6-eth3 tag=10
ovs-vsctl set port s8-eth3 tag=10
ovs-vsctl set port s9-eth3 tag=10

# vlan 11
ovs-vsctl set port s1-eth2 tag=11
ovs-vsctl set port s9-eth4 tag=11

ovs-vsctl set port s1-eth3 trunk=9
ovs-vsctl set port s2-eth1 trunk=9

ovs-vsctl set port s1-eth4 trunk=9
ovs-vsctl set port s4-eth1 trunk=9

ovs-vsctl set port s2-eth4 trunk=9
ovs-vsctl set port s5-eth1 trunk=9

ovs-vsctl set port s4-eth3 trunk=9
ovs-vsctl set port s5-eth2 trunk=9

ovs-vsctl set port s5-eth5 trunk=10
ovs-vsctl set port s6-eth2 trunk=10

ovs-vsctl set port s5-eth6 trunk=10
ovs-vsctl set port s8-eth1 trunk=10

ovs-vsctl set port s6-eth4 trunk=10
ovs-vsctl set port s9-eth1 trunk=10

ovs-vsctl set port s8-eth4 trunk=10
ovs-vsctl set port s9-eth2 trunk=10
