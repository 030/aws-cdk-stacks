#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { ScanImageAndSendEmailStack } from '../lib/scan_image_and_send_email-stack';

const app = new cdk.App();
new ScanImageAndSendEmailStack(app, 'ScanImageAndSendEmailStack');
