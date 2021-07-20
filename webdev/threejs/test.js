
const scene = new THREE.Scene();

scene.background = new THREE.Color(0x000000);

const camera = new THREE.PerspectiveCamera(
    75, window.innerWidth / window.innerHeight, 0.1, 1000
);


  // Set up lights
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
  scene.add(ambientLight);

  const dirLight = new THREE.DirectionalLight(0xffffff, 0.6);
  dirLight.position.set(10, 20, 0);
  scene.add(dirLight);


const renderer = new THREE.WebGLRenderer({antialias: true});

renderer.setSize(window.innerWidth-10, window.innerHeight-10);

document.body.appendChild(renderer.domElement);

const geometry = new THREE.BoxGeometry(2, 2, 2);

const texture = new THREE.TextureLoader().load('textures/crate.gif');

const material = new THREE.MeshBasicMaterial({map : texture });
const cube = new THREE.Mesh(geometry, material);




scene.add(cube);


camera.position.z = 5;

function animate(){

    requestAnimationFrame(animate);

    renderer.render(scene, camera);

    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;



    if (cube.position.x > 9){
        cube.position.x = -9;
    };

}

animate();

window.addEventListener('keydown', (event) =>{
    const key = event.key;
    if (key == "ArrowLeft"){
        cube.rotation.y -= 0.1;
        cube.position.x -= 0.1;
    }
    else if (key == "ArrowRight"){
        cube.rotation.y += 0.1;
        cube.position.x += 0.1;
    }
    else if (key == "ArrowUp"){
        cube.rotation.x += 0.1;
        cube.position.y += 0.1;
    }
    else if (key == "ArrowDown"){
        cube.rotation.x -= 0.1;
        cube.position.y -= 0.1;
    }
    else if (key.code == 32){
        cube.rotation.x -= 0.1;
        cube.position.y -= 0.1;
    }
    
});
