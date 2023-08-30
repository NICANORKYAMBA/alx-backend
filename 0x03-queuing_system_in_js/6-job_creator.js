// Import necessary modules
import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Define the job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'This is a test notification message'
};

// Create a job and add it to the queue
const job = queue.create('push_notification_code', jobData);

// Event handler for a successfully created job
job.on('complete', () => {
  console.log('Notification job completed');
});

// Event handler for a failed job
job.on('failed', () => {
  console.log('Notification job failed');
});

// Save the job to the queue
job.save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  } else {
    console.error('Error creating job:', err);
  }

  // Exit the script
  process.exit(0);
});
