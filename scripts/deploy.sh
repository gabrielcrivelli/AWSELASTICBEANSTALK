#!/bin/bash
set -e
echo "Deploying to AWS Elastic Beanstalk..."
eb deploy
echo "✅ Deploy complete!"
