export default function FileUploader({files,setFiles}){

function handleChange(e){

setFiles(Array.from(e.target.files));

}

return(

<div className="card">

<h2>📂 Upload Files</h2>

<input
type="file"
multiple
onChange={handleChange}
/>

<br/><br/>

{files.map(file=>(

<div className="file-item" key={file.name}>

📄 {file.name}

</div>

))}

</div>

);

}