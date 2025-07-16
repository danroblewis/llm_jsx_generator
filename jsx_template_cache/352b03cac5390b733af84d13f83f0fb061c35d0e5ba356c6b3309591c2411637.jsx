<div
  style={{
    backgroundColor: '#212121',
    color: '#bdbdbd',
    padding: '10px',
    borderRadius: '5px',
    width: '800px',
    fontFamily: ' monospace',
    fontSize: '12px',
    boxShadow: '0 2px 5px rgba(0, 0, 0, 0.3)',
  }}
>
  <h2
    style={{
      color: '#f0f0f0',
      borderBottom: '1px solid #333',
      paddingBottom: '5px',
      margin: '0 0 10px 0',
    }}
  >
    Network Interface Data
  </h2>

  <div style={{ display: 'flex', justifyContent: 'space-between' }}>
    <div
      style={{ width: '48%', backgroundColor: '#333', padding: '5px', borderRadius: '5px' }}
    >
      <h3
        style={{
          color: '#e0e0e0',
          borderBottom: '1px solid #444',
          paddingBottom: '3px',
          margin: '0 -10px 5px 0',
        }}
      >
        WiFi Network Info
      </h3>
      <ul>
        <li>SSID: <span style={{ textOverflow: 'ellipsis', whiteSpace: 'nowrap', width: '150px', display: 'inline-block' }}>{props.ssid}</span></li>
        <li>Frequency: {props.frequency}</li>
        <li>Signal Strength: {props.signal_strength} dBm</li>
      </ul>
    </div>

    <div
      style={{
        width: '48%',
        backgroundColor: '#333',
        padding: '5px',
        borderRadius: '5px',
      }}
    >
      <h3
        style={{
          color: '#e0e0e0',
          borderBottom: '1px solid #444',
          paddingBottom: '3px',
          margin: '0 -10px !important',
        }}
      >
        Counters
      </h3>
      <ul>
        <li>Total Packets Sent: {props.transmit_packets_total}</li>
        <li>Total Packets Received: {props.receive_packets_total}</li>
      </ul>
    </div>
  </div>

  <div
    style={{
      display: 'flex',
      justifyContent: 'space-between',
      marginTop: '10px'
    }}
  >
    <div
      style={{
        width: '32%',
        backgroundColor: '#333',
        padding: '5px',
        borderRadius: '5px',
      }}
    >
      <h3
        style={{
          color: '#e0e0e0',
          borderBottom: '1px solid #444',
          paddingBottom: '3px',
          margin: '0 -10px 5px 0',
        }}
      >
        Transmit Data
      </h3>
      <ul>
        <li>Speed: {props.transmit_speed}</li>
        <li>Packets per Second: {props.transmit_pps}</li>
      </ul>
    </div>

    <div
      style={{
        width: '32%',
        backgroundColor: '#333',
        padding: '5px',
        borderRadius: '5px',
      }}
    >
      <h3
        style={{
          color: '#e0e0e0',
          borderBottom: '1px solid #444',
          paddingBottom: '3px',
          margin: '0 -10px 10px 0',
        }}
      >
        Receive Data
      </h3>
      <ul>
        <li>Speed: {props.receive_speed}</li>
        <li>Packets per Second: {props.receive_pps}</li>
      </ul>
    </div>
    <div
      style={{
        width: '32%',
        backgroundColor: '#333',
        padding: '5px',
        borderRadius: '5px',
      }}
    >
      <h3
        style={{
          color: '#e0e0e0',
          borderBottom: '1px solid #444',
          paddingBottom: '3px',
          margin: '0 -10px 10px 0',
        }}
      >
        Bytes
      </h3>
      <ul>
        <li>Bytes Sent: {props.bytes_sent}</li>
        <li>Bytes Recieved: {props.bytes_recieved}</li>
      </ul>
    </div>
  </div>

  <div
    style={{
      display: 'flex',
      justifyContent: 'space-between',
      marginTop: '10px'
    }}
  >
    <div
      style={{
        width: '48%',
        backgroundColor: '#333',
        padding: '5px',
        borderRadius: '5px',
      }}
    >
      <h3
        style={{
          color: '#e0e0e0',
          borderBottom: '1px solid #444',
          paddingBottom: '3px',
          margin: '0 -10px 5px 0',
        }}
      >
        Station List
      </h3>
      <ul>
        {props.station_list &&
          props.station_list.map((station, index) => (
            <li key={index}>{station.mac_address} - {station.rssi} dBm</li>
          ))}
      </ul>
    </div>
    <div
      style={{
        width: '48%',
        backgroundColor: '#333',
        padding: '5px',
        borderRadius: '5px',
      }}
    >
      <h3
        style={{
          color: '#e0e0e0',
          borderBottom: '1px solid #444',
          paddingBottom: '3px',
          margin: '0 -10px  3px 0',
        }}
      >
        Network Configuration
      </h3>
      <ul>
        <li>IP Address: {props.ip_address}</li>
        <li>Subnet Mask: {props.subnet_mask}</li>
        <li>Gateway: {props.gateway}</li>
      </ul>
    </div>
  </div>
</div>