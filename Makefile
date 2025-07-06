shell:
	nix develop
render:
	manim-slides convert SCENE scene.html -ccontrols=true
