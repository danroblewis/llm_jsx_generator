<div style={{ backgroundColor: '#222', color: '#00c698', padding: '10px', borderRadius: '5px', width: '600px' }}>
  <h2 style={{ fontSize: '1.2em', marginBottom: '10px', textOverflow: 'ellipsis', overflow: 'hidden', whiteSpace: 'nowrap' }}>System Metrics</h2>

  <div style={{ display: 'flex', flexWrap: 'wrap' }}>

    <div style={{ width: '30%', padding: '5px', boxSizing: 'border-box' }}>
      <p style={{ fontSize: '0.8em', margin: '0 0 5px', textOverflow: 'ellipsis', overflow: 'hidden', whiteSpace: 'nowrap' }}>CPU Usage</p>
      <div style={{ width: '100%', height: '15px', backgroundColor: '#444', borderRadius: '7.5px', overflow: 'hidden' }}>
        <div style={{ width: `${props.cpu.percent_used}%`, height: '100%', backgroundColor: '#00c698' }} />
      </div>
      <p style={{ fontSize: '0.7em', textAlign: 'center', marginTop: '0px' }}>{props.cpu.percent_used.toFixed(1)}%</p>
      <p style={{ fontSize: '0.6em' }}>1min: {props.cpu.load_averages.1min.toFixed(2)}</p>
      <p style={{ fontSize: '0.6em' }}>5min: {props.cpu.load_averages.5min.toFixed(2)}</p>
      <p style={{ fontSize: '0.6em' }}>15min: {props.cpu.load_ averages.15min.toFixed(2)}</p>
    </div>

    <div style={{ width: '30%', padding: '5px', boxSizing: 'border-box' }}>
      <p style={{ fontSize: '0.8em', margin: '0 &nbsp;0 &nbsp;5px', textOverflow: 'ellipsis', overflow: 'hidden', whiteSpace: 'nowrap' }}>Memory Usage</p>
      <div style={{ width: '100%', height: '15px', backgroundColor: '#444', borderRadius: '7.5px', overflow: 'hidden' }}>
        <div style={{ width: `${(props.memory.used / props.memory.total) * 100}%`, height: '100%', backgroundColor: '#00c698' }} />
      </div>
      <p style={{ fontSize: '0.7em', textAlign: 'center', marginTop: '0px' }}>{props.memory.percent_used.toFixed(1)}%</p>
      <p style={{ fontSize: '0.6em' }}>Total: {formatBytes(props.memory.total)}</p>
      <p style={{ fontSize: '0.6em' }}>Free: {formatBytes(props.memory.free)}</p>
    </div>

    <div style={{ width: '40%', padding: '5px', boxSizing: 'border-box' }}>
      <p style={{ fontSize: '0.8em', margin: '0 0 5px', textOverflow: 'ellipsis', overflow: 'hidden', whiteSpace: 'nowrap' }}>Disk Usage</p>
      <div style={{ width: '100%', height: '15px', backgroundColor: '#444', borderRadius: '7.5px', overflow: 'hidden' }}>
        <div style={{ width: `${(props.disk.used / props.disk.total) *   100}%`, height: '100%', backgroundColor: '#00c698' }} />
      </div>
      <p style={{ fontSize: '0.7em', textAlign: 'center', marginTop: '0px' }}>{props.disk.percent_used.toFixed(1)}%</p>
      <p style={{ fontSize: '0.6em' }}>Total: {formatBytes(props.disk.total)}</p>
      <p style={{ fontSize: '0.6em' }}>Free: {formatBytes(props.disk.free)}</p>
    </div>
  </div>

  <div style={{ marginTop: '10px' }}>
    <p style={{ fontSize: '0.8em', margin: '0 0 5px', textOverflow: 'ellipsis', overflow: 'hidden', whiteSpace: 'nowrap' }}>Uptime</p>
    <p style={{ fontSize: '0.7em' }}>Seconds: {props.uptime.seconds.toFixed(2)}</p>
    <p style={{ fontSize: '0.7em' }}>Days: {props.uptime.days.toFixed(2)}</p>
    <p style={{ fontSize: '0.7em' }}>Hours: {props.uptime.hours.toFixed(2)}</p>
  </div>
</div>