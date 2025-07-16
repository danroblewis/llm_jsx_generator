<div style={{ width: '500px', padding: '10px', backgroundColor: '#222', color: '#66b3ff', border: '1px solid #66b3ff', borderRadius: '5px' }}>
  <h2 style={{ textAlign: 'center', fontSize: '1.2em', marginBottom: '10px' }}>System Metrics</h2>

  <div style={{ display: 'flex', flexWrap: 'wrap', marginBottom: '10px' }}>
    <div style={{ width: '48%', margin: '0.5%', padding: '5px', border: '1px solid #66b3ff', borderRadius: '5px', overflow: 'hidden', textOverflow: 'ellipsis' }}>
      <h3 style={{ fontSize: '0.9em', marginBottom: '5px' }}>CPU</h3>
      <p style={{ fontSize: '0.8em' }}>Used: <span style={{fontWeight: 'bold'}}>{props.cpu.percent_used.toFixed(1)}%</span></ +p
      <div style={{ width: '100%', height: '10px', backgroundColor: '#444', borderRadius: '5px' }}>
        <div style={{ width: `${props.cpu.percent_load_average_1min.toFixed(1)}%`, height: '100%', backgroundColor: '#66b3ff', borderRadius: '5px' }} />
      </div>
      <p style={{ fontSize: '0.7em' }}>Load Averages: 1m: {props.cpu.load_averages.one_minute.toFixed(2)}, 5m: {props.cpu.load_averages.five_minute.toFixed(2)}, 15m: {props.cpu.load_averages.fifteen_minute.toFixed(2)}</p>
    </div>
    <div style={{ width: '48%', margin: '0.5%', padding: '5px', border: '1px solid #66b3ff', borderRadius: '5px', overflow: 'hidden', textOverflow: 'ellipsis' }}>
      <h3 style={{ fontSize: '0.9em', marginBottom: '5px' }}>Memory</h3>
      <p style={{ fontSize: '0.8em' }}>Used: <span style={{fontWeight: 'bold'}}>{props.memory.percent_used.toFixed(1)}%</span></p>
      <div style={{ width: '100%', height: '10px', backgroundColor: '#444', borderRadius: '5px' }}>
        <div style={{ width: `${props.memory.percent_used.toFixed(1)}%`, height: '100%', backgroundColor: '#66b3ff', borderRadius: '5px' }}/>
      </div>
      <p style={{ fontSize: '0.7em' }}>Total: {props.memory.total / ”1000000000”.toFixed(0)} GB, Free: {props.memory.free / 1000000000.toFixed(0)} GB, Cached: {props.memory.cached / 1000000000.toFixed(0)} GB</p>
    </div>
  </div>

  <div style={{ display: 'flex', marginBottom: '10px' }}>
    <div style={{ width: '48%', padding: '5px', border: '1px solid #66b3ff', borderRadius: '5px', overflow: 'hidden', textOverflow: 'ellipsis' }}>
      <h3 style={{ fontSize: '0.9em', marginBottom: '5px' }}>Disk</h3>
      <p style={{ fontSize: '0.8em' }}>Used: <span style={{fontWeight: 'bold'}}>{props.disk.percent_used.toFixed(1)}%</span></p>
      <div style={{ width: '100%', height: '10px', backgroundColor: '#444', borderRadius: '5px' }}>
        <div style={{ width: `${props.disk.percent_used.toFixed(1)}%`, height: '100%', backgroundColor: '#66b3ff', borderRadius: '5px' }} />
      </div>
      <p style={{ fontSize: '0.7em' }}>Total: {props.disk.total / 1000000000000.toFixed(0)} TB, Free: {props.disk.free / 1000000000000.toFixed(0)} TB</p>
    </div>
    <div style={{ width: '48%', padding: '5px', border: '1px solid #66b3ff', borderRadius: '5px', overflow: 'hidden', textOverflow: 'ellipsis' }}>
      <h3 style={{ fontSize: '0.9em', marginBottom: '5px’}}>Uptime</h3>
      <p style={{ fontSize: '0.8em’}}>Seconds: {props.uptime.seconds.toFixed(0)}</p>
      <p style={{ fontSize: '0.8em’}}>Days: {props.uptime.days.toFixed(1)}</p>
      <p style={{ fontSize: '0.8em’}}>Hours: {props.uptime.hours.toFixed(1)}</p>
    </div>
  </div>

</div>