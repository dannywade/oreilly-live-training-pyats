# pyATS and Genie CLI

- `genie parse {command}`
- `genie learn`
- `genie diff`
- `pyats shell`

# Genie CLI

## Parse

Parse the "show version" Cisco IOS-XE command output: ```uv run genie parse "show version" --learn-hostname --testbed-file testbed.yml```

### Example Output

```json
0%|                                                                                                                                                                   | 0/1 [00:00<?, ?it/s]
{
  "version": {
    "chassis": "C8000V",
    "chassis_sn": "9VNZGF5ZOKE",
    "compiled_by": "mcpre",
    "compiled_date": "Wed 30-Nov-22 02:47",
    "copyright_years": "1986-2022",
    "curr_config_register": "0x2102",
    "disks": {
      "bootflash:.": {
        "disk_size": "5234688",
        "type_of_disk": "virtual hard disk"
      }
    },
    "hostname": "Router-1718",
    "image_id": "X86_64_LINUX_IOSD-UNIVERSALK9-M",
    "image_type": "production image",
    "label": "RELEASE SOFTWARE (fc4)",
    "last_reload_reason": "reload",
    "license_type": "Perpetual",
    "location": "Cupertino",
    "main_mem": "1979691",
    "mem_size": {
      "non-volatile configuration": "32768",
      "physical": "3964728"
    },
    "number_of_intfs": {
      "Gigabit Ethernet": "3"
    },
    "os": "IOS-XE",
    "platform": "Virtual XE",
    "processor_type": "VXE",
    "returned_to_rom_by": "reload",
    "rom": "IOS-XE ROMMON",
    "router_operating_mode": "Autonomous",
    "rtr_type": "C8000V",
    "system_image": "bootflash:packages.conf",
    "uptime": "1 day, 19 hours, 11 minutes",
    "uptime_this_cp": "1 day, 19 hours, 12 minutes",
    "version": "17.9.2a",
    "version_short": "17.9",
    "xe_version": "17.09.02a"
  }
}
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  1.10it/s]
```

### Command

Parse two Cisco IOS-XE commands: ```uv run genie parse "show version" "show interfaces" --learn-hostname --testbed-file testbed.yml```

### Example Output

```json
  0%|                                                                                                                                           | 0/2 [00:00<?, ?it/s]{
{
  "version": {
    "chassis": "C8000V",
    "chassis_sn": "9VNZGF5ZOKE",
    "compiled_by": "mcpre",
    "compiled_date": "Wed 30-Nov-22 02:47",
    "copyright_years": "1986-2022",
    "curr_config_register": "0x2102",
    "disks": {
      "bootflash:.": {
        "disk_size": "5234688",
        "type_of_disk": "virtual hard disk"
      }
    },
    "hostname": "Router-1718",
    "image_id": "X86_64_LINUX_IOSD-UNIVERSALK9-M",
    "image_type": "production image",
    "label": "RELEASE SOFTWARE (fc4)",
    "last_reload_reason": "reload",
    "license_type": "Perpetual",
    "location": "Cupertino",
    "main_mem": "1979691",
    "mem_size": {
      "non-volatile configuration": "32768",
      "physical": "3964728"
    },
    "number_of_intfs": {
      "Gigabit Ethernet": "3"
    },
    "os": "IOS-XE",
    "platform": "Virtual XE",
    "processor_type": "VXE",
    "returned_to_rom_by": "reload",
    "rom": "IOS-XE ROMMON",
    "router_operating_mode": "Autonomous",
    "rtr_type": "C8000V",
    "system_image": "bootflash:packages.conf",
    "uptime": "1 day, 19 hours, 13 minutes",
    "uptime_this_cp": "1 day, 19 hours, 14 minutes",
    "version": "17.9.2a",
    "version_short": "17.9",
    "xe_version": "17.09.02a"
  }
}
 50%|█████████████████████████████████████████████████████████████████████████████▌                                                                             | 1/2 [00:00<00:00,  1.12it/s]{
  "GigabitEthernet1": {
    "arp_timeout": "04:00:00",
    "arp_type": "arpa",
    "auto_negotiate": true,
    "bandwidth": 1000000,
    "counters": {
      "in_broadcast_pkts": 0,
      "in_crc_errors": 0,
      "in_errors": 0,
      "in_frame": 0,
      "in_giants": 0,
      "in_ignored": 0,
      "in_mac_pause_frames": 0,
      "in_multicast_pkts": 0,
      "in_no_buffer": 0,
      "in_octets": 166252987,
      "in_overrun": 0,
      "in_pkts": 1315347,
      "in_runts": 0,
      "in_throttles": 0,
      "in_watchdog": 0,
      "last_clear": "never",
      "out_babble": 0,
      "out_broadcast_pkts": 0,
      "out_buffer_failure": 0,
      "out_buffers_swapped": 0,
      "out_collision": 0,
      "out_deferred": 0,
      "out_errors": 0,
      "out_interface_resets": 0,
      "out_late_collision": 0,
      "out_lost_carrier": 0,
      "out_mac_pause_frames": 0,
      "out_multicast_pkts": 0,
      "out_no_carrier": 0,
      "out_octets": 249605140,
      "out_pkts": 1440353,
      "out_underruns": 0,
      "out_unknown_protocl_drops": 0,
      "rate": {
        "in_rate": 8000,
        "in_rate_pkts": 8,
        "load_interval": 300,
        "out_rate": 9000,
        "out_rate_pkts": 7
      }
    },
    "delay": 10,
    "description": "NETCONF Demo - 2025-11-16 11:48:22",
    "duplex_mode": "full",
    "enabled": true,
    "encapsulations": {
      "encapsulation": "arpa"
    },
    "flow_control": {
      "receive": false,
      "send": false
    },
    "ipv4": {
      "10.10.20.148/24": {
        "ip": "10.10.20.148",
        "prefix_length": "24"
      }
    },
    "is_deleted": false,
    "keepalive": 10,
    "last_input": "00:00:00",
    "last_output": "00:00:00",
    "line_protocol": "up",
    "link_type": "auto",
    "mac_address": "0050.56bf.280f",
    "media_type": "Virtual",
    "mtu": 1500,
    "oper_status": "up",
    "output_hang": "never",
    "phys_address": "0050.56bf.280f",
    "port_channel": {
      "port_channel_member": false
    },
    "port_speed": "1000mbps",
    "queues": {
      "input_queue_drops": 0,
      "input_queue_flushes": 0,
      "input_queue_max": 375,
      "input_queue_size": 1,
      "output_queue_max": 40,
      "output_queue_size": 0,
      "queue_strategy": "fifo",
      "total_output_drop": 0
    },
    "reliability": "255/255",
    "rxload": "1/255",
    "txload": "1/255",
    "type": "vNIC"
  },
  "GigabitEthernet2": {
    "arp_timeout": "04:00:00",
    "arp_type": "arpa",
    "auto_negotiate": true,
    "bandwidth": 1000000,
    "counters": {
      "in_broadcast_pkts": 0,
      "in_crc_errors": 0,
      "in_errors": 0,
      "in_frame": 0,
      "in_giants": 0,
      "in_ignored": 0,
      "in_mac_pause_frames": 0,
      "in_multicast_pkts": 0,
      "in_no_buffer": 0,
      "in_octets": 14340,
      "in_overrun": 0,
      "in_pkts": 239,
      "in_runts": 0,
      "in_throttles": 0,
      "in_watchdog": 0,
      "last_clear": "never",
      "out_babble": 0,
      "out_broadcast_pkts": 0,
      "out_buffer_failure": 0,
      "out_buffers_swapped": 0,
      "out_collision": 0,
      "out_deferred": 0,
      "out_errors": 0,
      "out_interface_resets": 12,
      "out_late_collision": 0,
      "out_lost_carrier": 5,
      "out_mac_pause_frames": 0,
      "out_multicast_pkts": 0,
      "out_no_carrier": 0,
      "out_octets": 1260,
      "out_pkts": 21,
      "out_underruns": 0,
      "out_unknown_protocl_drops": 0,
      "rate": {
        "in_rate": 0,
        "in_rate_pkts": 0,
        "load_interval": 300,
        "out_rate": 0,
        "out_rate_pkts": 0
      }
    },
    "delay": 10,
    "duplex_mode": "full",
    "enabled": true,
    "encapsulations": {
      "encapsulation": "dot1q",
      "first_dot1q": "1"
    },
    "flow_control": {
      "receive": false,
      "send": false
    },
    "ipv4": {
      "172.168.120.1/24": {
        "ip": "172.168.120.1",
        "prefix_length": "24"
      }
    },
    "is_deleted": false,
    "keepalive": 10,
    "last_input": "12:31:56",
    "last_output": "18:38:59",
    "line_protocol": "up",
    "link_type": "auto",
    "mac_address": "0050.56bf.034d",
    "media_type": "Virtual",
    "mtu": 1500,
    "oper_status": "up",
    "output_hang": "never",
    "phys_address": "0050.56bf.034d",
    "port_channel": {
      "port_channel_member": false
    },
    "port_speed": "1000mbps",
    "queues": {
      "input_queue_drops": 0,
      "input_queue_flushes": 0,
      "input_queue_max": 375,
      "input_queue_size": 0,
      "output_queue_max": 40,
      "output_queue_size": 0,
      "queue_strategy": "fifo",
      "total_output_drop": 0
    },
    "reliability": "255/255",
    "rxload": "1/255",
    "txload": "1/255",
    "type": "vNIC"
  },
  "GigabitEthernet2.100": {
    "arp_timeout": "04:00:00",
    "arp_type": "arpa",
    "bandwidth": 1000000,
    "delay": 10,
    "description": "Subinterfaz DEMO VLAN 100",
    "enabled": true,
    "encapsulations": {
      "encapsulation": "dot1q",
      "first_dot1q": "100"
    },
    "is_deleted": false,
    "keepalive": 10,
    "line_protocol": "up",
    "mac_address": "0050.56bf.034d",
    "mtu": 1500,
    "oper_status": "up",
    "phys_address": "0050.56bf.034d",
    "port_channel": {
      "port_channel_member": false
    },
    "reliability": "255/255",
    "rxload": "1/255",
    "txload": "1/255",
    "type": "vNIC"
  },
  "GigabitEthernet3": {
    "arp_timeout": "04:00:00",
    "arp_type": "arpa",
    "auto_negotiate": true,
    "bandwidth": 1000000,
    "counters": {
      "in_broadcast_pkts": 0,
      "in_crc_errors": 0,
      "in_errors": 0,
      "in_frame": 0,
      "in_giants": 0,
      "in_ignored": 0,
      "in_mac_pause_frames": 0,
      "in_multicast_pkts": 0,
      "in_no_buffer": 0,
      "in_octets": 1560,
      "in_overrun": 0,
      "in_pkts": 26,
      "in_runts": 0,
      "in_throttles": 0,
      "in_watchdog": 0,
      "last_clear": "never",
      "out_babble": 0,
      "out_broadcast_pkts": 0,
      "out_buffer_failure": 0,
      "out_buffers_swapped": 0,
      "out_collision": 0,
      "out_deferred": 0,
      "out_errors": 0,
      "out_interface_resets": 4,
      "out_late_collision": 0,
      "out_lost_carrier": 2,
      "out_mac_pause_frames": 0,
      "out_multicast_pkts": 0,
      "out_no_carrier": 0,
      "out_octets": 0,
      "out_pkts": 0,
      "out_underruns": 0,
      "out_unknown_protocl_drops": 0,
      "rate": {
        "in_rate": 0,
        "in_rate_pkts": 0,
        "load_interval": 300,
        "out_rate": 0,
        "out_rate_pkts": 0
      }
    },
    "delay": 10,
    "duplex_mode": "full",
    "enabled": false,
    "encapsulations": {
      "encapsulation": "arpa"
    },
    "flow_control": {
      "receive": false,
      "send": false
    },
    "is_deleted": false,
    "keepalive": 10,
    "last_input": "18:38:37",
    "last_output": "never",
    "line_protocol": "down",
    "link_type": "auto",
    "mac_address": "0050.56bf.be29",
    "media_type": "Virtual",
    "mtu": 1500,
    "oper_status": "down",
    "output_hang": "never",
    "phys_address": "0050.56bf.be29",
    "port_channel": {
      "port_channel_member": false
    },
    "port_speed": "1000mbps",
    "queues": {
      "input_queue_drops": 0,
      "input_queue_flushes": 0,
      "input_queue_max": 375,
      "input_queue_size": 0,
      "output_queue_max": 40,
      "output_queue_size": 0,
      "queue_strategy": "fifo",
      "total_output_drop": 0
    },
    "reliability": "255/255",
    "rxload": "1/255",
    "txload": "1/255",
    "type": "vNIC"
  },
  "Loopback200": {
    "bandwidth": 8000000,
    "counters": {
      "in_abort": 0,
      "in_broadcast_pkts": 0,
      "in_crc_errors": 0,
      "in_errors": 0,
      "in_frame": 0,
      "in_giants": 0,
      "in_ignored": 0,
      "in_multicast_pkts": 0,
      "in_no_buffer": 0,
      "in_octets": 0,
      "in_overrun": 0,
      "in_pkts": 0,
      "in_runts": 0,
      "in_throttles": 0,
      "last_clear": "never",
      "out_broadcast_pkts": 0,
      "out_buffer_failure": 0,
      "out_buffers_swapped": 0,
      "out_collision": 0,
      "out_errors": 0,
      "out_interface_resets": 0,
      "out_multicast_pkts": 0,
      "out_octets": 0,
      "out_pkts": 0,
      "out_underruns": 0,
      "out_unknown_protocl_drops": 0,
      "rate": {
        "in_rate": 0,
        "in_rate_pkts": 0,
        "load_interval": 300,
        "out_rate": 0,
        "out_rate_pkts": 0
      }
    },
    "delay": 5000,
    "description": "manual config",
    "enabled": true,
    "encapsulations": {
      "encapsulation": "loopback"
    },
    "is_deleted": false,
    "keepalive": 10,
    "last_input": "never",
    "last_output": "never",
    "line_protocol": "up",
    "mtu": 1514,
    "oper_status": "up",
    "output_hang": "never",
    "port_channel": {
      "port_channel_member": false
    },
    "queues": {
      "input_queue_drops": 0,
      "input_queue_flushes": 0,
      "input_queue_max": 75,
      "input_queue_size": 0,
      "output_queue_max": 0,
      "output_queue_size": 0,
      "queue_strategy": "fifo",
      "total_output_drop": 0
    },
    "reliability": "255/255",
    "rxload": "1/255",
    "txload": "1/255",
    "type": "Loopback"
  }
}
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:01<00:00,  1.10it/s]
```

## Learn

### Command

Learn all the device features: ```uv run genie learn all --learn-hostname --testbed-file testbed.yml --output full_capture```

### Example Output

```
Learning '['acl', 'arp', 'bgp', 'device', 'dot1x', 'eigrp', 'fdb', 'hsrp', 'igmp', 'interface', 'isis', 'lag', 'lisp', 'lldp', 'management', 'mcast', 'mld', 'msdp', 'nd', 'ntp', 'ospf', 'pim', 'platform', 'prefix_list', 'rip', 'route_policy', 'routing', 'static_routing', 'stp', 'terminal', 'utils', 'vlan', 'vrf', 'vxlan', 'config']' on devices '['cat8000v']'
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 35/35 [01:52<00:00,  3.22s/it]
+==============================================================================+
| Genie Learn Summary for device cat8000v                                      |
+==============================================================================+
|  Connected to cat8000v                                                       |
|  -   Log: full_capture/connection_cat8000v.txt                               |
|------------------------------------------------------------------------------|
|  Learnt feature 'acl'                                                        |
|  -  Ops structure:  full_capture/acl_iosxe_cat8000v_ops.txt                  |
|  -  Device Console: full_capture/acl_iosxe_cat8000v_console.txt              |
|------------------------------------------------------------------------------|
|  Learnt feature 'arp'                                                        |
|  -  Ops structure:  full_capture/arp_iosxe_cat8000v_ops.txt                  |
|  -  Device Console: full_capture/arp_iosxe_cat8000v_console.txt              |
|------------------------------------------------------------------------------|
|  Learnt feature 'bgp'                                                        |
|  -  Ops structure:  full_capture/bgp_iosxe_cat8000v_ops.txt                  |
|  -  Device Console: full_capture/bgp_iosxe_cat8000v_console.txt              |
|------------------------------------------------------------------------------|
|  Learnt feature 'device'                                                     |
|  -  Ops structure:  full_capture/device_iosxe_cat8000v_ops.txt               |
|  -  Device Console: full_capture/device_iosxe_cat8000v_console.txt           |
|------------------------------------------------------------------------------|
|  Learnt feature 'dot1x'                                                      |
|  -  Ops structure:  full_capture/dot1x_iosxe_cat8000v_ops.txt                |
|  -  Device Console: full_capture/dot1x_iosxe_cat8000v_console.txt            |
|------------------------------------------------------------------------------|
|  Learnt feature 'eigrp'                                                      |
|  -  Ops structure:  full_capture/eigrp_iosxe_cat8000v_ops.txt                |
|  -  Device Console: full_capture/eigrp_iosxe_cat8000v_console.txt            |
|------------------------------------------------------------------------------|
|  Learnt feature 'fdb'                                                        |
|  -  Ops structure:  full_capture/fdb_iosxe_cat8000v_ops.txt                  |
|  -  Device Console: full_capture/fdb_iosxe_cat8000v_console.txt              |
|------------------------------------------------------------------------------|
|  Learnt feature 'hsrp'                                                       |
|  -  Ops structure:  full_capture/hsrp_iosxe_cat8000v_ops.txt                 |
|  -  Device Console: full_capture/hsrp_iosxe_cat8000v_console.txt             |
|------------------------------------------------------------------------------|
|  Learnt feature 'igmp'                                                       |
|  -  Ops structure:  full_capture/igmp_iosxe_cat8000v_ops.txt                 |
|  -  Device Console: full_capture/igmp_iosxe_cat8000v_console.txt             |
|------------------------------------------------------------------------------|
|  Learnt feature 'interface'                                                  |
|  -  Ops structure:  full_capture/interface_iosxe_cat8000v_ops.txt            |
|  -  Device Console: full_capture/interface_iosxe_cat8000v_console.txt        |
|------------------------------------------------------------------------------|
|  Learnt feature 'isis'                                                       |
|  -  Ops structure:  full_capture/isis_iosxe_cat8000v_ops.txt                 |
|  -  Device Console: full_capture/isis_iosxe_cat8000v_console.txt             |
|------------------------------------------------------------------------------|
|  Learnt feature 'lag'                                                        |
|  -  Ops structure:  full_capture/lag_iosxe_cat8000v_ops.txt                  |
|  -  Device Console: full_capture/lag_iosxe_cat8000v_console.txt              |
|------------------------------------------------------------------------------|
|  Learnt feature 'lisp'                                                       |
|  -  Ops structure:  full_capture/lisp_iosxe_cat8000v_ops.txt                 |
|  -  Device Console: full_capture/lisp_iosxe_cat8000v_console.txt             |
|------------------------------------------------------------------------------|
|  Learnt feature 'lldp'                                                       |
|  -  Ops structure:  full_capture/lldp_iosxe_cat8000v_ops.txt                 |
|  -  Device Console: full_capture/lldp_iosxe_cat8000v_console.txt             |
|------------------------------------------------------------------------------|
|  Could not learn feature 'management'                                        |
|  -  Exception:      full_capture/management_iosxe_cat8000v_exception.txt     |
|  -  Ops structure:  full_capture/management_iosxe_cat8000v_ops.txt           |
|  -  Device Console: full_capture/management_iosxe_cat8000v_console.txt       |
|------------------------------------------------------------------------------|
|  Learnt feature 'mcast'                                                      |
|  -  Ops structure:  full_capture/mcast_iosxe_cat8000v_ops.txt                |
|  -  Device Console: full_capture/mcast_iosxe_cat8000v_console.txt            |
|------------------------------------------------------------------------------|
|  Learnt feature 'mld'                                                        |
|  -  Ops structure:  full_capture/mld_iosxe_cat8000v_ops.txt                  |
|  -  Device Console: full_capture/mld_iosxe_cat8000v_console.txt              |
|------------------------------------------------------------------------------|
|  Learnt feature 'msdp'                                                       |
|  -  Ops structure:  full_capture/msdp_iosxe_cat8000v_ops.txt                 |
|  -  Device Console: full_capture/msdp_iosxe_cat8000v_console.txt             |
|------------------------------------------------------------------------------|
|  Learnt feature 'nd'                                                         |
|  -  Ops structure:  full_capture/nd_iosxe_cat8000v_ops.txt                   |
|  -  Device Console: full_capture/nd_iosxe_cat8000v_console.txt               |
|------------------------------------------------------------------------------|
|  Learnt feature 'ntp'                                                        |
|  -  Ops structure:  full_capture/ntp_iosxe_cat8000v_ops.txt                  |
|  -  Device Console: full_capture/ntp_iosxe_cat8000v_console.txt              |
|------------------------------------------------------------------------------|
|  Learnt feature 'ospf'                                                       |
|  -  Ops structure:  full_capture/ospf_iosxe_cat8000v_ops.txt                 |
|  -  Device Console: full_capture/ospf_iosxe_cat8000v_console.txt             |
|------------------------------------------------------------------------------|
|  Learnt feature 'pim'                                                        |
|  -  Ops structure:  full_capture/pim_iosxe_cat8000v_ops.txt                  |
|  -  Device Console: full_capture/pim_iosxe_cat8000v_console.txt              |
|------------------------------------------------------------------------------|
|  Learnt feature 'platform'                                                   |
|  -  Ops structure:  full_capture/platform_iosxe_cat8000v_ops.txt             |
|  -  Device Console: full_capture/platform_iosxe_cat8000v_console.txt         |
|------------------------------------------------------------------------------|
|  Learnt feature 'prefix_list'                                                |
|  -  Ops structure:  full_capture/prefix_list_iosxe_cat8000v_ops.txt          |
|  -  Device Console: full_capture/prefix_list_iosxe_cat8000v_console.txt      |
|------------------------------------------------------------------------------|
|  Learnt feature 'rip'                                                        |
|  -  Ops structure:  full_capture/rip_iosxe_cat8000v_ops.txt                  |
|  -  Device Console: full_capture/rip_iosxe_cat8000v_console.txt              |
|------------------------------------------------------------------------------|
|  Learnt feature 'route_policy'                                               |
|  -  Ops structure:  full_capture/route_policy_iosxe_cat8000v_ops.txt         |
|  -  Device Console: full_capture/route_policy_iosxe_cat8000v_console.txt     |
|------------------------------------------------------------------------------|
|  Learnt feature 'routing'                                                    |
|  -  Ops structure:  full_capture/routing_iosxe_cat8000v_ops.txt              |
|  -  Device Console: full_capture/routing_iosxe_cat8000v_console.txt          |
|------------------------------------------------------------------------------|
|  Learnt feature 'static_routing'                                             |
|  -  Ops structure:  full_capture/static_routing_iosxe_cat8000v_ops.txt       |
|  -  Device Console: full_capture/static_routing_iosxe_cat8000v_console.txt   |
|------------------------------------------------------------------------------|
|  Could not learn feature 'stp'                                               |
|  -  Exception:      full_capture/stp_iosxe_cat8000v_exception.txt            |
|  -  Ops structure:  full_capture/stp_iosxe_cat8000v_ops.txt                  |
|  -  Device Console: full_capture/stp_iosxe_cat8000v_console.txt              |
|------------------------------------------------------------------------------|
|  Learnt feature 'terminal'                                                   |
|  -  Ops structure:  full_capture/terminal_iosxe_cat8000v_ops.txt             |
|  -  Device Console: full_capture/terminal_iosxe_cat8000v_console.txt         |
|------------------------------------------------------------------------------|
|  Could not learn feature 'utils'                                             |
|  -  Exception:      full_capture/utils_iosxe_cat8000v_exception.txt          |
|  -  Feature not yet developed for this os                                    |
|------------------------------------------------------------------------------|
|  Learnt feature 'vlan'                                                       |
|  -  Ops structure:  full_capture/vlan_iosxe_cat8000v_ops.txt                 |
|  -  Device Console: full_capture/vlan_iosxe_cat8000v_console.txt             |
|------------------------------------------------------------------------------|
|  Learnt feature 'vrf'                                                        |
|  -  Ops structure:  full_capture/vrf_iosxe_cat8000v_ops.txt                  |
|  -  Device Console: full_capture/vrf_iosxe_cat8000v_console.txt              |
|------------------------------------------------------------------------------|
|  Learnt feature 'vxlan'                                                      |
|  -  Ops structure:  full_capture/vxlan_iosxe_cat8000v_ops.txt                |
|  -  Device Console: full_capture/vxlan_iosxe_cat8000v_console.txt            |
|------------------------------------------------------------------------------|
|  Learnt feature 'config'                                                     |
|  -  Ops structure:  full_capture/config_iosxe_cat8000v_ops.txt               |
|  -  Device Console: full_capture/config_iosxe_cat8000v_console.txt           |
|==============================================================================|
```

## Diff

### Command


To demonstrate `genie diff`, make a configuration change on the device and re-learn the device features. The output will be saved to the folder `full_capture_loop_chg/`.

Configuration change:
```
interface Loopback150
ip address 172.16.20.1 255.255.255.0
```

Re-learn the device features: ```uv run genie learn all --learn-hostname --testbed-file testbed.yml --output full_capture_loop_chg```

Diff two 'genie learn' capture outputs: ```uv run genie diff full_capture full_capture_loop_chg --output full_capture_diff```

### Example Output
```
+==============================================================================+
| Genie Diff Summary between directories full_capture/ and                     |
| full_capture_loop_chg/                                                       |
+==============================================================================+
|  File: bgp_iosxe_cat8000v_ops.txt                                            |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
|  File: device_iosxe_cat8000v_ops.txt                                         |
|   - Diff can be found at full_capture_diff/diff_device_iosxe_cat8000v_ops.txt |
|------------------------------------------------------------------------------|
|  File: mld_iosxe_cat8000v_ops.txt                                            |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
|  File: config_iosxe_cat8000v_ops.txt                                         |
|   - Diff can be found at full_capture_diff/diff_config_iosxe_cat8000v_ops.txt |
|------------------------------------------------------------------------------|
|  File: vlan_iosxe_cat8000v_ops.txt                                           |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
|  File: routing_iosxe_cat8000v_ops.txt                                        |
|   - Diff can be found at                                                     |
| full_capture_diff/diff_routing_iosxe_cat8000v_ops.txt                        |
|------------------------------------------------------------------------------|
|  File: nd_iosxe_cat8000v_ops.txt                                             |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
|  File: vxlan_iosxe_cat8000v_ops.txt                                          |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
|  File: static_routing_iosxe_cat8000v_ops.txt                                 |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
|  File: lisp_iosxe_cat8000v_ops.txt                                           |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
|  File: eigrp_iosxe_cat8000v_ops.txt                                          |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
|  File: acl_iosxe_cat8000v_ops.txt                                            |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
|  File: rip_iosxe_cat8000v_ops.txt                                            |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
|  File: stp_iosxe_cat8000v_ops.txt                                            |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
|  File: msdp_iosxe_cat8000v_ops.txt                                           |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
|  File: arp_iosxe_cat8000v_ops.txt                                            |
|   - Diff can be found at full_capture_diff/diff_arp_iosxe_cat8000v_ops.txt   |
|------------------------------------------------------------------------------|
|  File: prefix_list_iosxe_cat8000v_ops.txt                                    |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
|  File: route_policy_iosxe_cat8000v_ops.txt                                   |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
|  File: ospf_iosxe_cat8000v_ops.txt                                           |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
|  File: dot1x_iosxe_cat8000v_ops.txt                                          |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
|  File: hsrp_iosxe_cat8000v_ops.txt                                           |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
|  File: lag_iosxe_cat8000v_ops.txt                                            |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
|  File: fdb_iosxe_cat8000v_ops.txt                                            |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
|  File: management_iosxe_cat8000v_ops.txt                                     |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
|  File: terminal_iosxe_cat8000v_ops.txt                                       |
|   - Diff can be found at                                                     |
| full_capture_diff/diff_terminal_iosxe_cat8000v_ops.txt                       |
|------------------------------------------------------------------------------|
|  File: interface_iosxe_cat8000v_ops.txt                                      |
|   - Diff can be found at                                                     |
| full_capture_diff/diff_interface_iosxe_cat8000v_ops.txt                      |
|------------------------------------------------------------------------------|
|  File: igmp_iosxe_cat8000v_ops.txt                                           |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
|  File: pim_iosxe_cat8000v_ops.txt                                            |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
|  File: ntp_iosxe_cat8000v_ops.txt                                            |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
|  File: mcast_iosxe_cat8000v_ops.txt                                          |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
|  File: isis_iosxe_cat8000v_ops.txt                                           |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
|  File: lldp_iosxe_cat8000v_ops.txt                                           |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
|  File: platform_iosxe_cat8000v_ops.txt                                       |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
|  File: vrf_iosxe_cat8000v_ops.txt                                            |
|   - Identical                                                                |
|------------------------------------------------------------------------------|
```

### Config Feature Diff

```
--- full_capture/config_iosxe_cat8000v_ops.txt
+++ full_capture_loop_chg/config_iosxe_cat8000v_ops.txt
+interface Loopback150:
+ ip address 172.16.20.1 255.255.255.0:
```

### Interface Feature Diff

```
--- full_capture/interface_iosxe_cat8000v_ops.txt
+++ full_capture_loop_chg/interface_iosxe_cat8000v_ops.txt
 info:
+ Loopback150:
+  bandwidth: 8000000
+  counters:
+   in_broadcast_pkts: 0
+   in_crc_errors: 0
+   in_errors: 0
+   in_multicast_pkts: 0
+   in_octets: 0
+   in_pkts: 0
+   last_clear: never
+   out_broadcast_pkts: 0
+   out_errors: 0
+   out_multicast_pkts: 0
+   out_octets: 0
+   out_pkts: 0
+   rate:
+    in_rate: 0
+    in_rate_pkts: 0
+    load_interval: 300
+    out_rate: 0
+    out_rate_pkts: 0
+  delay: 5000
+  enabled: True
+  encapsulation:
+   encapsulation: loopback
+  ipv4:
+   172.16.20.1/24:
+    ip: 172.16.20.1
+    prefix_length: 24
+    secondary: False
+  mtu: 1514
+  oper_status: up
+  port_channel:
+   port_channel_member: False
+  switchport_enable: False
+  type: Loopback
```

# pyATS Blitz

The Blitz YAML file provides a simple example of configuring a loopback interface and verifying it's up. To execute the Blitz YAML file, run the following command:

```
uv run pyats run genie --trigger-datafile blitz.yml --trigger-uids 'TestLoopbackInterface' --testbed-file testbed.yml
```

You must specify the testcase UID of the tests you want to execute. Fortunately, we only have one testcase in `blitz.yml` (`TestLoopbackInterface`).

## Blitz Results

Here's a quick look at what the test results should look like:

```
2025-07-13T02:44:45: %EASYPY-INFO: +------------------------------------------------------------------------------+
2025-07-13T02:44:45: %EASYPY-INFO: |                             Task Result Summary                              |
2025-07-13T02:44:45: %EASYPY-INFO: +------------------------------------------------------------------------------+
2025-07-13T02:44:45: %EASYPY-INFO: Task-1: genie_testscript                                                  FAILED
2025-07-13T02:44:45: %EASYPY-INFO: Task-1: genie_testscript.common_setup                                     PASSED
2025-07-13T02:44:45: %EASYPY-INFO: Task-1: genie_testscript.TestLoopbackInterface.uut                        PASSED
2025-07-13T02:44:45: %EASYPY-INFO: Task-1: genie_testscript.common_cleanup                                   FAILED
2025-07-13T02:44:45: %EASYPY-INFO: 
2025-07-13T02:44:45: %EASYPY-INFO: +------------------------------------------------------------------------------+
2025-07-13T02:44:45: %EASYPY-INFO: |                             Task Result Details                              |
2025-07-13T02:44:45: %EASYPY-INFO: +------------------------------------------------------------------------------+
2025-07-13T02:44:45: %EASYPY-INFO: Task-1: genie_testscript                                                  FAILED
2025-07-13T02:44:45: %EASYPY-INFO: |-- common_setup                                                          PASSED
2025-07-13T02:44:45: %EASYPY-INFO: |   |-- connect                                                           PASSED
2025-07-13T02:44:45: %EASYPY-INFO: |   |-- configure                                                        SKIPPED
2025-07-13T02:44:45: %EASYPY-INFO: |   |-- configuration_snapshot                                            PASSED
2025-07-13T02:44:45: %EASYPY-INFO: |   |-- save_bootvar                                                      PASSED
2025-07-13T02:44:45: %EASYPY-INFO: |   |-- learn_system_defaults                                             PASSED
2025-07-13T02:44:45: %EASYPY-INFO: |   |-- initialize_traffic                                               SKIPPED
2025-07-13T02:44:45: %EASYPY-INFO: |   `-- PostProcessor-1                                                   PASSED
2025-07-13T02:44:45: %EASYPY-INFO: |-- TestLoopbackInterface.uut                                             PASSED
2025-07-13T02:44:45: %EASYPY-INFO: |   |-- apply_configuration                                               PASSED
2025-07-13T02:44:45: %EASYPY-INFO: |   |   |-- STEP 1: Starting action configure on device 'cat8000v'        PASSED
2025-07-13T02:44:45: %EASYPY-INFO: |   |   |-- STEP 1.1: Configuring 'cat8000v'                              PASSED
2025-07-13T02:44:45: %EASYPY-INFO: |   |   `-- STEP 2: Starting action sleep                                 PASSED
2025-07-13T02:44:45: %EASYPY-INFO: |   `-- verify_configuration                                              PASSED
2025-07-13T02:44:45: %EASYPY-INFO: |       |-- STEP 1: Starting action execute on device 'cat8000v'          PASSED
2025-07-13T02:44:45: %EASYPY-INFO: |       |-- STEP 1.1: Executing 'show ip interface brief' on 'cat8000v'   PASSED
2025-07-13T02:44:45: %EASYPY-INFO: |       |-- STEP 1.1.1: Verify that 'Loopback100' is included in th...    PASSED
2025-07-13T02:44:45: %EASYPY-INFO: |       |-- STEP 2: Starting action parse on device 'cat8000v'            PASSED
2025-07-13T02:44:45: %EASYPY-INFO: |       |-- STEP 2.1: Parsing 'show interfaces loopback100' on 'cat8000v' PASSED
2025-07-13T02:44:45: %EASYPY-INFO: |       `-- STEP 2.1.1: Verify that 'contains_key_value('oper_statu...    PASSED
2025-07-13T02:44:45: %EASYPY-INFO: `-- common_cleanup                                                        FAILED
2025-07-13T02:44:45: %EASYPY-INFO:     |-- verify_configuration_snapshot                                     FAILED
2025-07-13T02:44:45: %EASYPY-INFO:     |-- stop_traffic                                                     SKIPPED
2025-07-13T02:44:45: %EASYPY-INFO:     `-- PostProcessor-1                                                   PASSED
```

You'll notice the `common_cleanup` section failed. More specifically, you'll see the `verify_configuration_snapshot` test failed. That's due to the fact we configured a loopback interface during testing, but did not remove it. The `verify_configuration_snapshot` compares the device configuration snapshots captured during the `common_setup` and `common_cleanup` test sections to ensure the configuration is identical before and after testing.

```
2025-07-13T02:44:44: %GENIE-INFO:  | Check Post configuration Summary                                                                                                                   |
2025-07-13T02:44:44: %GENIE-INFO:  +====================================================================================================================================================+
2025-07-13T02:44:44: %GENIE-INFO:  | * Summary for device: cat8000v                                                                                                                        |
2025-07-13T02:44:44: %GENIE-ERROR: |     - Comparison between original configuration taken at common setup and the one taken at common cleanup is different as per the following diffs: |
2025-07-13T02:44:44: %GENIE-ERROR: | +interface Loopback100                                                                                                                             |
2025-07-13T02:44:44: %GENIE-ERROR: | + description Configured by Genie Blitz                                                                                                            |
2025-07-13T02:44:44: %GENIE-ERROR: | + no ip address                                                                                                                                    |
2025-07-13T02:44:44: %GENIE-INFO:  |****************************************************************************************************************************************************|
2025-07-13T02:44:44: %GENIE-INFO: 

2025-07-13T02:44:44: %AETEST-ERROR: Failed reason: Comparison of Configuration in Common Setup and Common Cleanup has been modified.  Check the summary table for more details
```