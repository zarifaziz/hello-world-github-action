# hello-world-github-action

Learning how to create and release a Github action

## Workflows

A workflow can run Github actions defined either within the current repo or 
from the actions marketplace. It can also run other commands.

## Actions

Actions contain specific logic of what you want to do. You can specify what the
inputs and outputs are and what you want to run in the action.

## ESBUILD / Bundlers

Actions usually depend on node modules, but we don't want to commit the
`node_modules/` directory to the repo so that actions have access to it. That's
why we use a bundler like esbuild to bundle everything into `dist/index.js` 
which contains everything the action needs to run.

Github recommends [`vercel/ncc](https://github.com/vercel/ncc) for compiling a
Node.js module into a single file together with all the dependencies, gcc-style.
