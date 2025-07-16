<div style={{ backgroundColor: '#222', color: '#0FF', padding: '10px', borderRadius: '5px', width: '500px', fontFamily: 'monospace', fontSize: '12px' }}>
  <div style={{ marginBottom: '10px', borderBottom: '1px solid #0FF' }}>
    <h3 style={{ margin: '0', fontSize: '14px', textOverflow: 'ellipsis', whiteSpace: 'nowrap', overflow: 'hidden' }}>System Metrics</h3>
  </div>

  <div style={{ display: 'flex', flexWrap: 'wrap', marginTop: '10px' }}>
    {/* CPU */}
    <div style={{ width: '30%', padding: '5px', boxSizing: 'border-box' }}>
      <div style={{ backgroundColor: '#333', padding: '5px', borderRadius: '3px' }}>
        <p style={{ margin: '0', fontSize: '10px' }}>CPU Usage</",
        <div style={{ width: '100%', height: '10px', backgroundColor: '#555' }}>
          <div style={{ width: `${props.cpu.percent_used}%`, height: '10px', backgroundColor: '#0F0' }}></div>
        </div>
        <p style={{ margin: '0', fontSize: '10px', textAlign: 'center' }}>{props.cpu.percent_used.toFixed(1)}%</p>
        <p style={{ margin: '0', fontSize: '8px' }}>Load Averages:</p>
        <ul style={{ margin: '0', padding: '0' }}>
          <li style={{ fontSize: '8px' }}>1min: {props.cpu.load_averages.1min.toFixed(2)}</li>
          <li style={{ fontSize: '8px' }}>5min: {props.cpu.load_averages.5min.toFixed(2)}</li>
          <li style={{ fontSize: '8px' }}>15min: {props.cpu.load_averages.1A15min.toFixed(2)}</li>
        </ul>
      </div>
    </div>

    {/* Memory */}
    <div style={{ width: '35%', padding: '5px', boxSizing: 'border-box' }}>
      <div style={{ backgroundColor: '#333', padding: '5px', borderRadius: '3px' }}>
        <p style={{ margin: '0', fontSize: '10px' }}>Memory Usage</.

        <div style={{ width: '100%', height: '10px', backgroundColor: '#555' }}>
          <div style={{ width: `${props.memory.percent_used}%`, height: '10px', backgroundColor: '#0FF`
        </div>
        <p style={{ margin: '0', fontSize: '10px', textAlign: 'center' }}>{props.memory.percent_used.toFixed(1)}%</p>
        <p style={{ margin: '0', fontSize: '8px' }}>Total: {props.memory.total / (1024 * 1024 * 1024).toFixed(1)} GB</p>
        <p style={{ margin: '0', fontSize: '8px' }}>Available: {props.memory.available / (1024 * 1024 * 1024).toFixed(1)} GB</p>
        <p style={{ margin: '0', fontSize: '8px' }}>Used: {props.memory.used / (1024 * 1024 * 1024).toFixed(1)} GB</p>
      </div>
    </div>

    {/* Disk */}
    <div style={{ width: '30%', padding: '5px', boxSizing: 'border-box' }}>
      <div style={{ backgroundColor: '#333', padding: '5px', borderRadius: '3px' }}>
        <p style={{ margin: '0', fontSize: '10px' }}>Disk Usage</p>
        <div style={{ width: '100%', height: '10px', backgroundColor: '#555' }}>
          <div style={{ width: `${props.disk.percent_used}%`, height: '10px', backgroundColor: '#FF0`
        </div>
        <p style={{ margin: '0', fontSize: '10px', textAlign: 'center' }}>{props.disk.percent_used.toFixed(1)}%</
        <p style={{ margin: '0', fontSize: '8px' }}>Total: {props.disk.total / (1024 * 1024 * 1024 * 1024).toFixed(1)} TB</p>
        <p style={{ margin: '0', fontSize: '8px' }}>Used: {props.disk.used / (1024 * 1024 * 1024 * 1024).toFixed(1)} TB</p>
        <p style={{ margin: '0', fontSize: '8px' }}>Available: {props.disk.free / (1024 * 1024 * 1024 * 1024).toFixed(1)} TB</p>
      </div>
    </div>
  </div>

  <div style={{ marginTop: '10px' }}>
    <p style={{ fontSize: '10px' }}>Uptime: {props.uptime.days.toFixed(2)} days, {props.uptime.hours.toFixed(1)} hours</p>
    <p style={{ fontSize: '8px' }}>Seconds: {props.uptime.seconds}</p>
  </div>
</div>