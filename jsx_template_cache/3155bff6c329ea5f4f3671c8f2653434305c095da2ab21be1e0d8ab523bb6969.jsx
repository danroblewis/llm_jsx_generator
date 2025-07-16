<div
  style={{
    backgroundColor: '#222',
    color: '#fff',
    padding: '10px',
    borderRadius: '5px',
    fontFamily: 'monospace',
    fontSize: '10px',
    width: '600px',
    boxShadow: '0 2px 4px rgba(0, 0, 0, 0.5)',
  }}
>
  <h3
    style={{
      borderBottom: '1px solid #fff',
      paddingBottom: '5px',
      textAlign: 'center',
      margin: '0 auto',
      width: '95%',
    }}
  >
    Network Interface Data
  </h3>

  <div style={{ display: 'flex', flexWrap: 'wrap' }}>

    <div style={{ width: '30%', padding: '5px' }}>
      <h4 style={{ margin: '0', fontSize: '9px' }}>WiFi Signal Strength</h4>
      <div
        style={{
          width: '100%',
          height: '15px',
          backgroundColor: '#444',
          borderRadius: '5px',
          overflow: 'hidden',
          position: 'relative',
        }}
      >
        <div
          style={{
            width: '70%',
            height: '100%',
            backgroundColor: '#00cc00',
            position: 'absolute',
          }}
        ></div>
        <div
          style={{
            position: 'absolute',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            color: '#fff',
          }}
        >
          -50 dBm
        </div>
      </div>
    </div>

    <div style={{ width: "30%", padding: "5px" }}>
      <h4 style={{ margin: "0", fontSize: "9px" }}>Connected Clients</h4>
      <div style={{
        width: "100%",
        height: "15px",
        backgroundColor: "#444",
        borderRadius: "5px",
        overflow: "hidden",
        position: "relative",
        border: "1px solid #666",
      }}>
        <div style={{
          width: "80%",
          height: "100%",
          backgroundColor: "#ff9900",
          position: "absolute",
        }}></div>
        <div style={{
          position: "absolute",
          top: "50%",
          left: "50%",
          transform: "translate(-50%, -50%)",
          color: "#fff",
        }}>
          12
        </div>
      </div>
    </div>

    <div style={{ width: "40%", padding: "5px" }}>
      <h4 style={{ margin: "0", fontSize: "9px" }}>Data Transfer Rate</h4>
      <div style={{
        width: "100%",
        height: "15px",
        backgroundColor: "#444",
 -webkit-border-radius: 5px;
 -moz-border-radius: 5px;
 border-radius: 5px;
 overflow: "hidden",
 position: "relative",
      }}>
        <div style={{
          width: "50%",
          height: "100%",
          backgroundColor: "#ff00ff",
          position: "absolute",
        }}></div>
        <div style={{
          position: "absolute",
          top: "50%",
          left: "50%",
          transform: "translate(-50%, -50%)",
          color: "#fff",
        }}>
          54 Mbps
        </div>
      </div>
    </div>
  </div>

  <div style={{ marginTop: '10px' }}>
    <h4 style={{ margin: '0', fontSize: '9px' }}>Station Statistics</h4>
    <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '8px' }}>
      <thead>
        <tr style={{ backgroundColor: '#333' }}>
          <th style={{ padding: '3px', border: '1px solid #444', width: '20%' }}>MAC Address</th>
          <th style={{ padding: '3px', border: '1px solid #444', width: '15%' }}>Transmit Packets</th>
          <th style={{ padding: '3px', border: '1px and #444', width: '15%' }}>Receive Packets</th>
          <th style={{ padding: '3px', border: '1px solid #444', width: '20%' }}>Data Transmitted</th>
          <th style={{ padding: '3px', border: '1px solid #444', width: '20%' }}>Data Received</th>
        </tr>
      </thead>
      <tbody>
        {/* Example data row - repeat for each station */}
        <tr style={{ backgroundColor: '#222' }}>
          <td style={{ padding: '3px', border: '1px solid #444' }}>00:11:22:33:44:55</td>
          <td style={{ padding: '3px', border: '1px solid #444' }}>2031</td>
          <td style={{ padding: '3px', border: '1px solid #444' }}>440417</td>
          <td style={{ padding: '3px', border: '1px solid #444' }}>1.2 MB</td>
          <td style={{ padding: '3px', border: '1px solid #444' }}>5.6 GB</td>
        </tr>
        <tr style={{ backgroundColor: '#222' }}>
          <td style={{ padding: '3px', border: '1px solid #444' }}>AA:BB:CC:DD:EE:FF</td>
          <td style={{ padding: '3px', border: '1px solid #444' }}>9353137</td>
          <td style={{ padding: '3px', border: '1px solid #444' }}>7217065</td>
          <td style={{ padding: '3px', border: '1 * solid #444' }}>6.8 GB</td>
          <td style={{ padding: '3px', border: '1 * solid #444' }}>4.2 GB</td>
        </tr>
        <tr style={{ backgroundColor: '#222' }}>
          <td style={{ padding: '3px', border: '1px solid #444' }}>12:34:56:78:90:AB</td>
          <td style={{ padding: '3px', border: '1px solid #444' }}>16329</td>
          <td style={{ padding: '3px', border: '1px solid #444' }}>48899</td>
          <td style={{ padding: '3px', border: '1 * solid #444' }}>1.5 MB</td>
          <td style={{ padding: '3px', border: '1 * solid #444' }}>1.1 GB</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>