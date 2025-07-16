<div style={{ backgroundColor: '#222', color: '#00FF00', padding: '10px', borderRadius: '5px', width: '300px', fontFamily: 'monospace', fontSize: '12px', border: '1px solid #00FF00' }}>
  <div style={{ marginBottom: '5px', fontWeight: 'bold' }}>LCARS Data Display</div>
  <div style={{ display: 'flex', flexDirection: 'column' }}>
    <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '2px' }}>
      <span style={{ fontWeight: 'bold' }}>Error:</span>
      <span style={{ fontSize: '0.8em', textOverflow: 'ellipsis', overflow: 'hidden', whiteSpace: 'nowrap', width: '200px' }}>{props.error}</span>
    </div>
  </div>
</div>